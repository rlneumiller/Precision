bl_info = {
    "name": "Precision",
    "author": "rlneumiler@gmail.com", "various blenderheads, the interwebs"
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > UI > Tools",
    "description": "Configure precision modeling settings",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

import os
import bpy
import bpy.utils.previews
    
class PRECISION_OT_func(bpy.types.Operator):
    bl_idname = "precision.func"
    bl_label = "Set mm precision"

    def execute(self, context):
        bpy.context.scene.unit_settings.scale_length = 0.001
        bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
        bpy.context.scene.unit_settings.mass_unit = 'GRAMS'
     
        space = bpy.context.space_data
        space.overlay.show_stats=True
        space.clip_end = 10000
        space.clip_start = 0.01   
        
        return {'FINISHED'}
    
class CUSTOM_PT_myPanel(bpy.types.Panel):
    bl_label = "Configure Precision"
    bl_idname = "OBJECT_PT_custom_panel"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_category = "Precision"

    def draw(self, context):
        global custom_icons
        layout = self.layout
        layout.operator(PRECISION_OT_func.bl_idname)
        



classes = (PRECISION_OT_func, CUSTOM_PT_myPanel)
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
    
    