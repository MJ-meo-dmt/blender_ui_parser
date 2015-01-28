import bpy


### Addon info ###
bl_info = \
    {
        "name" : "Logic Block",
        "author" : "MJ-meo-dmt",
        "version" : (1, 0, 0),
        "blender" : (2, 6, 9),
        "location" : "Properties",
        "description" :
            "Creates a 'datablock' to attach to the object.(use with: panda3d tags)",
        "warning" : "",
        "wiki_url" : "",
        "tracker_url" : "",
        "category" : "Game Engine",
    }
#################


def loadProps():
    scnType = bpy.types.Scene
    # single value properties.
    stringProp = bpy.props.StringProperty
    floatProp = bpy.props.FloatProperty
    intProp = bpy.props.IntProperty
    boolProp = bpy.props.BoolProperty
    
    ## DONO IF THERE IS A BETTER WAY IM STILL UBER NOOB WITH THIS>>> ##
    
    scnType.datablock_priority = intProp( name = "Priority",
                                       default = 70, min = 70, max = 200,
                                    description = "Used for tasks, higher is less important" )
    
    scnType.datablock_name = stringProp(  name="Name",
                                            default=" ",
                                description = "Any name, not important")
    
    scnType.datablock_model = stringProp(  name="Model Path",
                                            default=" ",
                                description = "External Model path to be used with this object")

    scnType.datablock_customScript = stringProp(  name="Custom Script",
                                            default=" ",
                                description = "Path to script for selected object")

    scnType.datablock_lookAt = stringProp(  name="LookAt",
                                            default=" ",
                                description = "Object name to lookAt esp used for spotlights")
    
    scnType.datablock_sendEvent = stringProp(name="SendEvent",
                                                default=" ",
                                                description="Name of the fire event(send), esp for buttons")

    scnType.datablock_recvEvent = stringProp(name="RecvEvent",
                                                default=" ",
                                                description="Name of the receive event(accept('recvEvent'))")

    scnType.datablock_color = stringProp(name="Color",
                                            default=" ",
                                            description="In floats the color the light will have")

    scnType.datablock_hpr = stringProp(name="HPR",
                                            default=" ",
                                            description="To overwrite the hpr on the object, sometimes it doesnt work \
                                                        in the parser")

    scnType.datablock_rotateAxis = stringProp(name="Rotate Axis",
                                                default=" ",
                                                description="Supply the rotate axis for the object ('x, y, z')")
    scnType.datablock_moveAxis = stringProp(name="Move Axis",
                                                default=" ",
                                                description="Supply the move axis for the object ('x, y, z')")

    scnType.datablock_gravity = stringProp(name="Gravity",
                                                default="0, 0, -9",
                                                description="Supply a gravity setting for the object or level.")

    scnType.datablock_moveForce = floatProp(name="Move Force",
                                                default=1.0,
                                                description="Supply a force amount for the object if needed")

    scnType.datablock_jumpForce = floatProp(name="Jump Force",
                                                default=1.0,
                                                description="Supply a force amount for the player usually")

    scnType.datablock_rotateAmount = floatProp(name="Rotate Amount",
                                                default=0.0,
                                                description="Supply a rotate amount for the object, degree")

    scnType.datablock_moveAmount = floatProp(name="Move Amount",
                                                default=0.0,
                                                description="Supply the amount to move the object, esp for lifts")

    scnType.datablock_state = boolProp(name="State",
                                        default=False,
                                        description="Set the state of the object")

    scnType.datablock_isCollisionMesh = boolProp(name="isCollisionMesh",
                                                    default=False,
                                                    description="Check for collision mesh")

    scnType.datablock_isBulletPlane = boolProp(name="isBulletPlane",
                                                default=False,
                                                description="Check to use bullet infinite plane")

    scnType.datablock_isDynamic = boolProp(name="isDynamic",
                                                default=False,
                                                description="Check for dynamic objects")

    scnType.datablock_pickable = boolProp(name="Pickable",
                                            default=False,
                                            description="Check for pickable objects")


    # triplet setup.... ( return value, name, description )
    EnumProperty = bpy.props.EnumProperty
    datablockTypes= [("playerType", "Player", "Player Type Datablock"),
                    ("cameraType", "Camera", "Camera Type Datablock"),
                    ("levelType", "Level", "Level Type Datablock"),
                    ("objectType", "Object", "Object Type Datablock"),
                    ("lightType", "Light", "Light Type Datablock"),
                    ("sensorType", "Sensor", "Sensor Type Datablock"),
                    ("doorType", "Door", "Door Type Datablock"),
                    ("liftType", "Lift", "Lift Type Datablock"),]
                    
    enumProp = EnumProperty( name = "Type", items = datablockTypes,
                    description = "Different Datablock types" )
    
    scnType.dropDownProp = enumProp
    
    ## Light type selection:
    # point, direct, ambient, spot
    lightTypes = [("pointType", "Point Light", "Point Light Type"),
                    ("directType", "Directional Light", "Directional Light Type"),
                    ("ambientType", "Ambient Light", "Ambient Light Type"),
                    ("spotType", "Spot Light", "Spot Light Type")]
                    
    lightControlType = EnumProperty( name = "Light Type", items = lightTypes,
                    description = "Choose a Light Type" )
  
    scnType.dropDownLight = lightControlType
    
    ## Level Type
    # Wall, Ground
    levelSubTypes = [("wallType", "Wall", "Make this object a Wall"),
                    ("groundType", "Ground", "Make this object a ground"),
                    ("complexType", "Complex", "Make this object a complex type"),
                    ("infoType", "Level Info", "Add info about level")]
                    
    LevelSubControlType = EnumProperty( name = "Level Type", items = levelSubTypes,
                    description = "Choose a Level Type" )
  
    scnType.dropDownLevelType = LevelSubControlType


  
class TypeSamplerPanel(bpy.types.Panel):
    bl_label = "Datablock"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "objectmode"
  
    def draw(self, context):
        scn = bpy.context.scene
        scnType = bpy.types.Scene
        layout = self.layout
        row = layout.row()
        col = row.column()
           
        ## SELECTION ##
        col.prop( scn, "dropDownProp" )
        
        ## CHECK PLAYER TYPE SELECTION ##
        if bpy.context.scene.dropDownProp == "playerType":
            col.prop( scn, "datablock_name" )
            col.prop( scn, "datablock_model" )
            col.prop( scn, "datablock_moveForce" )
            col.prop( scn, "datablock_jumpForce" )
            col.prop( scn, "datablock_customScript" )
            col.prop( scn, "datablock_state" )

        if bpy.context.scene.dropDownProp == "cameraType":
            col.prop( scn, "datablock_state" )
            col.prop( scn, "datablock_lookAt" )     
        
        ## CHECK LEVEL TYPE SELECTION ##
        if bpy.context.scene.dropDownProp == "levelType":
            col.prop( scn, "dropDownLevelType" ) # Subtype

            if bpy.context.scene.dropDownLevelType == "infoType":
                col.prop( scn, "datablock_name" )
                col.prop( scn, "datablock_gravity" )

            if bpy.context.scene.dropDownLevelType == "wallType":
                col.prop( scn, "datablock_isCollisionMesh" )
                col.prop( scn, "datablock_customScript" )

            if bpy.context.scene.dropDownLevelType == "groundType":
                col.prop( scn, "datablock_isBulletPlane" )
                col.prop( scn, "datablock_isCollisionMesh" )
                col.prop( scn, "datablock_customScript" )

            if bpy.context.scene.dropDownLevelType == "complexType":
                col.prop( scn, "datablock_isCollisionMesh" )
                col.prop( scn, "datablock_customScript" )
        
        ## CHECK OBJECT TYPE SELECTION ##
        if bpy.context.scene.dropDownProp == "objectType":
            col.prop( scn, "datablock_name" )
            col.prop( scn, "datablock_model" )
            col.prop( scn, "datablock_isDynamic" )
            col.prop( scn, "datablock_sendEvent" )
            col.prop( scn, "datablock_recvEvent" )
            col.prop( scn, "datablock_customScript" )
            col.prop( scn, "datablock_state" )
            col.prop( scn, "datablock_pickable" )

        ## CHECK SENSOR TYPE SELECTION ##
        if bpy.context.scene.dropDownProp == "sensorType":
            col.prop( scn, "datablock_name" )
            col.prop( scn, "dropdownSensorType" )
            col.prop( scn, "datablock_isDynamic" )
            col.prop( scn, "datablock_customScript" )
            col.prop( scn, "datablock_sendEvent" )
            col.prop( scn, "datablock_recvEvent" )
            col.prop( scn, "datablock_state" )
            col.prop( scn, "datablock_priority" )
            col.prop( scn, "datablock_gravity" )
        
        ## CHECK LIGHT TYPE SELECTION ##
        if bpy.context.scene.dropDownProp == "lightType":
            col.prop( scn, "dropDownLight" ) # Subtype
            if bpy.context.scene.dropDownLight == "pointType":
                col.prop( scn, "datablock_model" )
                col.prop( scn, "datablock_isDynamic" )
                col.prop( scn, "datablock_customScript" )
                col.prop( scn, "datablock_color" )
                col.prop( scn, "datablock_state" )
            
            if bpy.context.scene.dropDownLight == "directType":
                col.prop( scn, "datablock_customScript" )
                col.prop( scn, "datablock_color" )
                col.prop( scn, "datablock_hpr" )
                col.prop( scn, "datablock_state" )
                
            if bpy.context.scene.dropDownLight == "ambientType":
                col.prop( scn, "datablock_customScript" )
                col.prop( scn, "datablock_color" )
                col.prop( scn, "datablock_state" )
                
            if bpy.context.scene.dropDownLight == "spotType":
                col.prop( scn, "datablock_model" )
                col.prop( scn, "datablock_state" )
                col.prop( scn, "datablock_color" )
                col.prop( scn, "datablock_isDynamic" )
                col.prop( scn, "datablock_customScript" )
                col.prop( scn, "datablock_lookAt" )
                col.prop( scn, "datablock_hpr" )

        if bpy.context.scene.dropDownProp == "doorType":
            col.prop( scn, "datablock_name" )
            col.prop( scn, "datablock_isDynamic" )
            col.prop( scn, "datablock_customScript" )
            col.prop( scn, "datablock_sendEvent" )
            col.prop( scn, "datablock_recvEvent" )
            col.prop( scn, "datablock_rotateAmount" )
            col.prop( scn, "datablock_rotateAxis" )
            col.prop( scn, "datablock_state" )

        if bpy.context.scene.dropDownProp == "liftType":
            col.prop( scn, "datablock_name" )
            col.prop( scn, "datablock_isDynamic" )
            col.prop( scn, "datablock_state" )
            col.prop( scn, "datablock_sendEvent" )
            col.prop( scn, "datablock_recvEvent" )
            col.prop( scn, "datablock_moveAmount" )
            col.prop( scn, "datablock_moveForce" )
            col.prop( scn, "datablock_moveAxis" )
            col.prop( scn, "datablock_priority" )
        
        
        col.operator( "bpt.sample_op" )

  
class SampleOperator(bpy.types.Operator):
  
    bl_idname = "bpt.sample_op"
    bl_label = "Attach Datablock"
  
    def invoke(self, context, event ):
        # This will need some work.. because you can add doubles...
        #bpy.ops.object.game_property_new(type='FLOAT', name="")
        # Try to add something for adding a datablock to all selected objects
        # and then get the name of the objects and fill them into the name field
        datablockType = bpy.context.scene.dropDownProp
        lightType = bpy.context.scene.dropDownLight
        levelSubType = bpy.context.scene.dropDownLevelType
        activeObject = context.active_object
        
        # Check which datablock type is selected
        if datablockType == "playerType":
            # Write the datablock like in logic editor
            bpy.ops.object.game_property_new(type='STRING', name="player")
            bpy.ops.object.game_property_new(type='STRING', name="name")
            bpy.ops.object.game_property_new(type='STRING', name="model")
            bpy.ops.object.game_property_new(type='FLOAT', name="moveforce")
            bpy.ops.object.game_property_new(type='FLOAT', name="jumpforce")
            bpy.ops.object.game_property_new(type='STRING', name="customscript")
            bpy.ops.object.game_property_new(type='BOOL', name="state")
            
            # now add the values to them
            dict = activeObject.game.properties   
            dict['player'].value = "player"
            dict['name'].value = bpy.context.scene.datablock_name
            dict['model'].value = bpy.context.scene.datablock_model
            dict['moveforce'].value = bpy.context.scene.datablock_moveForce
            dict['jumpforce'].value = bpy.context.scene.datablock_jumpForce
            dict['customscript'].value = bpy.context.scene.datablock_customScript
            dict['state'].value = bpy.context.scene.datablock_state

        elif datablockType == "cameraType":
            bpy.ops.object.game_property_new(type='STRING', name="camera")
            bpy.ops.object.game_property_new(type='STRING', name="lookat")
            bpy.ops.object.game_property_new(type='BOOL', name="state")

            dict = activeObject.game.properties
            dict['camera'].value = "camera"
            dict['lookat'].value = bpy.context.scene.datablock_lookAt
            dict['state'].value = bpy.context.scene.datablock_state

        elif datablockType == "levelType":
            # Write the datablock like in logic editor

            if levelSubType == "infoType":
                bpy.ops.object.game_property_new(type='STRING', name="level")
                bpy.ops.object.game_property_new(type='STRING', name="name")
                bpy.ops.object.game_property_new(type='STRING', name="gravity")

                # now add the values to them
                dict = activeObject.game.properties   
                dict['level'].value = levelSubType
                dict['name'].value = bpy.context.scene.datablock_name
                dict['gravity'].value = bpy.context.scene.datablock_gravity

            if levelSubType == "wallType":
                bpy.ops.object.game_property_new(type='STRING', name="level")
                bpy.ops.object.game_property_new(type='BOOL', name="iscollisionmesh")
                bpy.ops.object.game_property_new(type='STRING', name="customscript")

                dict = activeObject.game.properties   
                dict['level'].value = levelSubType
                dict['iscollisionmesh'].value = bpy.context.scene.datablock_isCollisionMesh
                dict['customscript'].value = bpy.context.scene.datablock_customScript

            if levelSubType == "groundType":
                bpy.ops.object.game_property_new(type='STRING', name="level")
                bpy.ops.object.game_property_new(type='BOOL', name="iscollisionmesh")
                bpy.ops.object.game_property_new(type='BOOL', name="isbulletplane")
                bpy.ops.object.game_property_new(type='STRING', name="customscript")

                dict = activeObject.game.properties   
                dict['level'].value = levelSubType
                dict['iscollisionmesh'].value = bpy.context.scene.datablock_isCollisionMesh
                dict['isbulletplane'].value = bpy.context.scene.datablock_isBulletPlane
                dict['customscript'].value = bpy.context.scene.datablock_customScript

            if levelSubType == "complexType":
                bpy.ops.object.game_property_new(type='STRING', name="level")
                bpy.ops.object.game_property_new(type='BOOL', name="iscollisionmesh")

                dict = activeObject.game.properties   
                dict['level'].value = levelSubType
                dict['iscollisionmesh'].value = bpy.context.scene.datablock_isCollisionMesh
            
            
        elif datablockType == "objectType":
            # Write the datablock like in logic editor
            bpy.ops.object.game_property_new(type='STRING', name="object")
            bpy.ops.object.game_property_new(type='STRING', name="name")
            bpy.ops.object.game_property_new(type='STRING', name="model")
            bpy.ops.object.game_property_new(type='BOOL', name="isDynamic")
            bpy.ops.object.game_property_new(type='STRING', name="sendevent")
            bpy.ops.object.game_property_new(type='STRING', name="recvevent")
            bpy.ops.object.game_property_new(type='STRING', name="customscript")
            bpy.ops.object.game_property_new(type='BOOL', name="state")
            bpy.ops.object.game_property_new(type='BOOL', name="pickable")     
            
            # now add the values to them
            dict = activeObject.game.properties   
            dict['object'].value = "object"
            dict['name'].value = bpy.context.scene.datablock_name
            dict['model'].value = bpy.context.scene.datablock_model
            dict['isdynamic'].value = bpy.context.scene.datablock_isDynamic
            dict['sendevent'].value = bpy.context.scene.datablock_sendEvent
            dict['recvevent'].value = bpy.context.scene.datablock_recvEvent
            dict['customscript'].value = bpy.context.scene.datablock_customScript
            dict['state'].value = bpy.context.scene.datablock_state
            dict['pickable'].value = bpy.context.scene.datablock_pickable
            

        elif datablockType == "sensorType":
            # Write the datablock like in logic editor
            bpy.ops.object.game_property_new(type='STRING', name="sensor")
            bpy.ops.object.game_property_new(type='STRING', name="name")
            bpy.ops.object.game_property_new(type='BOOL', name="isdynamic")
            bpy.ops.object.game_property_new(type='STRING', name="customscript")
            bpy.ops.object.game_property_new(type='STRING', name="sendevent")
            bpy.ops.object.game_property_new(type='STRING', name="recvevent")
            bpy.ops.object.game_property_new(type='BOOL', name="state")
            bpy.ops.object.game_property_new(type='INT', name="priority")
            bpy.ops.object.game_property_new(type='STRING', name="gravity")
            
            # now add the values to them
            dict = activeObject.game.properties   
            dict['sensor'].value = "sensor"
            dict['name'].value = bpy.context.scene.datablock_name
            dict['isdynamic'].value = bpy.context.scene.datablock_isDynamic
            dict['customscript'].value = bpy.context.scene.datablock_customScript
            dict['sendevent'].value = bpy.context.scene.datablock_sendEvent
            dict['recvevent'].value = bpy.context.scene.datablock_recvEvent
            dict['state'].value = bpy.context.scene.datablock_state
            dict['priority'].value = bpy.context.scene.datablock_priority
            dict['gravity'].value = bpy.context.scene.datablock_gravity
            
        elif datablockType == "lightType":
            # POINT LIGHT PROP STUFF
            if lightType == "pointType":
                # Write the datablock like in logic editor
                bpy.ops.object.game_property_new(type='STRING', name="light")
                bpy.ops.object.game_property_new(type='STRING', name="model")
                bpy.ops.object.game_property_new(type='BOOL', name="isdynamic")
                bpy.ops.object.game_property_new(type='STRING', name="customscript")
                bpy.ops.object.game_property_new(type='STRING', name="color")
                bpy.ops.object.game_property_new(type='BOOL', name="state")
                
                # now add the values to them
                dict = activeObject.game.properties   
                dict['light'].value = lightType
                dict['model'].value = bpy.context.scene.datablock_model
                dict['isdynamic'].value = bpy.context.scene.datablock_isDynamic
                dict['customscript'].value = bpy.context.scene.datablock_customScript
                dict['color'].value = bpy.context.scene.datablock_color
                dict['state'].value = bpy.context.scene.datablock_state
            
            # DIRECTIONAL LIGHT PROP STUFF
            if lightType == "directType":
                # Write the datablock like in logic editor
                bpy.ops.object.game_property_new(type='STRING', name="light")
                bpy.ops.object.game_property_new(type='STRING', name="customscript")
                bpy.ops.object.game_property_new(type='STRING', name="color")
                bpy.ops.object.game_property_new(type='BOOL', name="state")
                bpy.ops.object.game_property_new(type='STRING', name="hpr")
                
                # now add the values to them
                dict = activeObject.game.properties   
                dict['light'].value = lightType
                dict['customscript'].value = bpy.context.scene.datablock_customScript
                dict['color'].value = bpy.context.scene.datablock_color
                dict['state'].value = bpy.context.scene.datablock_state
                dict['hpr'].value = bpy.context.scene.datablock_hpr

            
            # AMBIENT LIGHT PROP STUFF
            if lightType == "ambientType":
                # Write the datablock like in logic editor
                bpy.ops.object.game_property_new(type='STRING', name="light")
                bpy.ops.object.game_property_new(type='STRING', name="customscript")
                bpy.ops.object.game_property_new(type='STRING', name="color")
                bpy.ops.object.game_property_new(type='BOOL', name="state")
                
                # now add the values to them
                dict = activeObject.game.properties   
                dict['light'].value = lightType
                dict['customscript'].value = bpy.context.scene.datablock_customScript
                dict['color'].value = bpy.context.scene.datablock_color
                dict['state'].value = bpy.context.scene.datablock_state
            
            # SPOT LIGHT PROP STUFF
            if lightType == "spotType":
                # Write the datablock like in logic editor
                bpy.ops.object.game_property_new(type='STRING', name="light")
                bpy.ops.object.game_property_new(type='STRING', name="model")
                bpy.ops.object.game_property_new(type='STRING', name="customscript")
                bpy.ops.object.game_property_new(type='STRING', name="color")
                bpy.ops.object.game_property_new(type='BOOL', name="state")
                bpy.ops.object.game_property_new(type='STRING', name="hpr")
                bpy.ops.object.game_property_new(type='BOOL', name="isdynamic")
                bpy.ops.object.game_property_new(type='STRING', name="lookat")
                
                # now add the values to them
                dict = activeObject.game.properties   
                dict['light'].value = lightType
                dict['customscript'].value = bpy.context.scene.datablock_customScript
                dict['color'].value = bpy.context.scene.datablock_color
                dict['state'].value = bpy.context.scene.datablock_state
                dict['hpr'].value = bpy.context.scene.datablock_hpr
                dict['lookat'].value = bpy.context.scene.datablock_lookAt
                dict['isdynamic'].value = bpy.context.scene.datablock_isDynamic
                dict['model'].value = bpy.context.scene.datablock_model

        elif datablockType == "doorType":
            bpy.ops.object.game_property_new(type='STRING', name="door")
            bpy.ops.object.game_property_new(type='STRING', name="name")
            bpy.ops.object.game_property_new(type='BOOL', name="isdynamic")
            bpy.ops.object.game_property_new(type='STRING', name="customscript")
            bpy.ops.object.game_property_new(type='STRING', name="sendevent")
            bpy.ops.object.game_property_new(type='STRING', name="recvevent")
            bpy.ops.object.game_property_new(type='FLOAT', name="rotateamount")
            bpy.ops.object.game_property_new(type='STRING', name="rotateaxis")
            bpy.ops.object.game_property_new(type='BOOL', name="state")

            dict = activeObject.game.properties   
            dict['door'].value = "door"
            dict['name'].value = bpy.context.scene.datablock_name
            dict['isdynamic'].value = bpy.context.scene.datablock_isDynamic
            dict['customscript'].value = bpy.context.scene.datablock_customScript
            dict['sendevent'].value = bpy.context.scene.datablock_sendEvent
            dict['recvevent'].value = bpy.context.scene.datablock_recvEvent
            dict['rotateamount'].value = bpy.context.scene.datablock_rotateAmount
            dict['rotateaxis'].value = bpy.context.scene.datablock_rotateAxis
            dict['state'].value = bpy.context.scene.datablock_state

        elif datablockType == "liftType":
            bpy.ops.object.game_property_new(type='STRING', name="lift")
            bpy.ops.object.game_property_new(type='STRING', name="name")
            bpy.ops.object.game_property_new(type='BOOL', name="isdynamic")
            bpy.ops.object.game_property_new(type='STRING', name="customscript")
            bpy.ops.object.game_property_new(type='STRING', name="sendevent")
            bpy.ops.object.game_property_new(type='STRING', name="recvevent")
            bpy.ops.object.game_property_new(type='FLOAT', name="moveamount")
            bpy.ops.object.game_property_new(type='FLOAT', name="moveforce")
            bpy.ops.object.game_property_new(type='STRING', name="moveaxis")
            bpy.ops.object.game_property_new(type='BOOL', name="state")
            bpy.ops.object.game_property_new(type='INT', name="priority")

            dict = activeObject.game.properties   
            dict['lift'].value = "lift"
            dict['name'].value = bpy.context.scene.datablock_name
            dict['isdynamic'].value = bpy.context.scene.datablock_isDynamic
            dict['customscript'].value = bpy.context.scene.datablock_customScript
            dict['sendevent'].value = bpy.context.scene.datablock_sendEvent
            dict['recvevent'].value = bpy.context.scene.datablock_recvEvent
            dict['moveamount'].value = bpy.context.scene.datablock_moveAmount
            dict['moveforce'].value = bpy.context.scene.datablock_moveForce
            dict['moveaxis'].value = bpy.context.scene.datablock_moveAxis
            dict['state'].value = bpy.context.scene.datablock_state
            dict['priority'].value = bpy.context.scene.datablock_priority


        
        return {'FINISHED'}


def register():
    bpy.utils.register_class( TypeSamplerPanel )
    bpy.utils.register_class( SampleOperator )
 
 
def unregister():
    bpy.utils.register_class( TypeSamplerPanel )
    bpy.utils.register_class( SampleOperator )


 
 
if __name__ == "__main__":
    register()
    loadProps()
    