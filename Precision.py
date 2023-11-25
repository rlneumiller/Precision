bl_info = {
    "name": "Precision",
    "author": "rlneumiler@gmail.com",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > UI > Tools",
    "description": "Configure precision modeling settings",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

import os
import bpy

class PRECISION_OT_Func(bpy.types.Operator):
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
        
        grid_scale_to_mm()
        return {'FINISHED'}

import bpy

class VIEW3D_PT_PrecisionPanel(bpy.types.Panel):
    bl_label = "Configure Precision"
    bl_idname = "VIEW3D_PT_PrecisionPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = "UI"
    bl_category = "Precision"

    def draw(self, context):
        layout = self.layout
        layout.operator(PRECISION_OT_Func.bl_idname)

def grid_scale_to_mm():
    """Set grid scale to mm in 3D view areas."""
    for window in bpy.data.window_managers[0].windows:
        for area in window.screen.areas:
            if area.type != 'VIEW_3D':
                continue

            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.overlay.grid_scale = 0.001
                    break

classes = (PRECISION_OT_Func, VIEW3D_PT_PrecisionPanel)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
