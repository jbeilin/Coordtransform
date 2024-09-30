"""
/***************************************************************************
 Coordtransform
                                 A QGIS plugin
 transform input coordinate to whatever new refrence system using EPSG number
                              -------------------
        begin                : 2012-03-03
        latest changes       : 2018-04-17
        copyright            : (C) 2012-2018 by Giuseppe De Marco
        email                : demarco.giuseppe@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from __future__ import absolute_import
from builtins import str
from builtins import object
# Import the PyQt and QGIS libraries
from qgis.core import *
from qgis.PyQt.QtCore import *
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtWidgets import *
# Initialize Qt resources from file resources.py
from . import resources
#import pdb
# Import the code for the dialog
from .coordtransformdialog import CoordtransformDialog
import re

class Coordtransform(object):

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.dlg = CoordtransformDialog()
        x = None
        y = None
        input = None
        output = None
        chkout = 0
        chkin = 0
        self.invalidCrs = self.dlg.ui.mQgsProjectionSelectionWidgetINPUT.crs()
        
    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/coordtransform/icon.png"), \
            "Coordtransform_ENSG", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)
        
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&d2gis", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&d2gis",self.action)
        self.iface.removeToolBarIcon(self.action)
        
#custom functions begin------------------------------------------------------------
    def check_x(self):
        x = self.dlg.ui.X.text()
        if  x =='':
            QMessageBox.critical(None,"!","Please provide X/lon value")
            chkx = 0
        else:
            chkx = 1
        return chkx
    
    def check_y(self):
        y = self.dlg.ui.Y.text()
        if  y == '':
            QMessageBox.critical(None,"!","Please provide Y/lat value")
            chky = 0
        else:
            chky = 1
        return chky
    
    def check_input(self):
        
        print("Input CRS :", self.dlg.ui.mQgsProjectionSelectionWidgetINPUT.crs())
        # print("CrsNotSet",self.dlg.ui.mQgsProjectionSelectionWidgetINPUT.CrsNotSet)
        # print("Invalid",self.dlg.ui.mQgsProjectionSelectionWidgetINPUT.Invalid)
        
        if  re.search('invalid', str(self.dlg.ui.mQgsProjectionSelectionWidgetINPUT.crs()), re.IGNORECASE):
            QMessageBox.critical(None,"!","Please select an input CRS")
            chkin = 0
        else:
            chkin = 1
        return chkin
    
    def check_output(self):

        print("Output CRS :", self.dlg.ui.mQgsProjectionSelectionWidgetOUTPUT.crs())        
        # print("CrsNotSet",self.dlg.ui.mQgsProjectionSelectionWidgetOUTPUT.CrsNotSet)
        # print("Invalid",self.dlg.ui.mQgsProjectionSelectionWidgetOUTPUT.Invalid)
        
        if  re.search('invalid', str(self.dlg.ui.mQgsProjectionSelectionWidgetOUTPUT.crs()), re.IGNORECASE):
            QMessageBox.critical(None,"!","Please select an output CRS")
            chkout = 0
        else:
            chkout = 1
        return chkout
            
    
    def clear(self):
        self.dlg.ui.results.clear()
        self.dlg.ui.X.clear()
        self.dlg.ui.Y.clear()
        self.dlg.ui.inputproj4.clear()
        self.dlg.ui.outputproj4.clear()
        self.dlg.ui.trfY.clear()
        self.dlg.ui.trfX.clear()
        
        # a modifier : non fonctionnel
        self.dlg.ui.mQgsProjectionSelectionWidgetINPUT.setCrs(self.invalidCrs)
        self.dlg.ui.mQgsProjectionSelectionWidgetOUTPUT.setCrs(self.invalidCrs)
        self.dlg.ui.mQgsProjectionSelectionWidgetINPUT.update()

    
    def transform(self):
        #pyqtRemoveInputHook()
        #pdb.set_trace() 
        #self.dlg.ui.results.setText("Transform pressed\n")
        chkx = 0
        chky = 0
        chkin = 0
        chkout = 0
        chkx = self.check_x()
        chky = self.check_y()
        chkin = self.check_input()
        chkout = self.check_output()
        chk = chkx + chky + chkin + chkout
    
        
        if chk == 4:
            
            self.dlg.ui.results.clear()
            self.dlg.ui.inputproj4.clear()
            self.dlg.ui.outputproj4.clear()
            
            x = self.dlg.ui.X.text()
            y = self.dlg.ui.Y.text()
            
 
            crsSrc = self.dlg.ui.mQgsProjectionSelectionWidgetINPUT.crs()
            crsDest = self.dlg.ui.mQgsProjectionSelectionWidgetOUTPUT.crs()
            
            print(crsSrc.bounds())
            print(crsDest.bounds())
            
            # self.dlg.ui.results.setText("input CRS "+crsSrc.authid()+"\n"+"output CRS "+crsDest.authid())
            
            self.dlg.ui.inputproj4.setText(str(crsSrc.toProj4()))
            self.dlg.ui.outputproj4.setText(str(crsDest.toProj4()))
            
            context = QgsProject.instance()
            xform = QgsCoordinateTransform(crsSrc, crsDest, context)
            
            print(xform.coordinateOperation())
            print(xform.instantiatedCoordinateOperationDetails().proj)
            
            transfpoint=xform.transform(QgsPointXY(float(x),float(y)))
            
            self.dlg.ui.results.append("Pipeline : %s\n" % xform.instantiatedCoordinateOperationDetails().proj)
            
            if crsDest.isGeographic():
                strCoordFormat = "%.8f"
            else:
                strCoordFormat = "%.4f"
                
            self.dlg.ui.results.append("New coordinates : (%s, %s)" % (strCoordFormat % transfpoint.x(), strCoordFormat % transfpoint.y()))
            
            self.dlg.ui.trfX.setText(strCoordFormat % transfpoint.x())
            self.dlg.ui.trfY.setText(strCoordFormat % transfpoint.y())
        else:
            return

    # run method that performs all the real work
    def run(self):
        #Buttons events
        self.dlg.ui.clear.clicked.connect(self.clear)
        self.dlg.ui.transform.clicked.connect(self.transform)
        
        self.dlg.show()
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass
