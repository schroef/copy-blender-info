#######################################################

## Copy Blender Info	######
##
## v0.0.1
## Added
## 23-02-19 - Initial start addon & repo

## v0.0.2
## Added
## 23-02-19 - Feedback when data is copied (info sysbar)

## v0.0.3
## Changed
## 23-02-19 - Now using BL internal copy method, easier and less files (Thanks Oleg Stepanov)

bl_info = {
	"name": "Copy Blender Info",
	"description": "Copies Blender info such asversion, hash, date & time commit. This is handy for when filing a bug",
	"location": "Help Menu > Copy Blender Info",
	"author": "Rombout Versluijs",
	"version": (0, 0, 3),
	"blender": (2, 80, 0),
	"wiki_url": "https://github.com/schroef/copy-blender-info",
	"tracker_url": "https://github.com/schroef/copy-blender-info/issues",
	"category": "User"
}

import bpy

from bpy.types import (
	Operator
	)


class CAI_OT_CopyInfo(Operator):
	"""Copies Blender info to clipboard which is need to file a bug report"""
	bl_idname="cai.copy_info"
	bl_label="Copy Blender Info"

	def execute(self,context):
		version = bpy.app.version_string
		build = bpy.app.build_branch
		comDate = bpy.app.build_commit_date
		comTime = bpy.app.build_commit_time
		buildHash = bpy.app.build_hash
		buildType = bpy.app.build_type

		appInfo = version+", "+buildHash.decode()+", "+comDate.decode()+" "+comTime.decode()
		bpy.context.window_manager.clipboard=appInfo
		self.report({'INFO'}, 'Info copied, ready to paste :)')
		return {'FINISHED'}


def CAI_AddCopyOP(self, context):
	self.layout.operator("cai.copy_info",text="Copy Blender Info", icon='COPYDOWN')

classes = (
	CAI_OT_CopyInfo
)


def register():
	#for cls in classes:
	#	bpy.utils.register_class(cls)
	bpy.utils.register_class(CAI_OT_CopyInfo)

	bpy.types.TOPBAR_MT_help.prepend(CAI_AddCopyOP)

def unregister():
	bpy.types.TOPBAR_MT_help.remove(CAI_AddCopyOP)
	#for cls in reversed(classes):
	#	bpy.utils.unregister_class(cls)
	bpy.utils.unregister_class(CAI_OT_CopyInfo)

if __name__ == "__main__":
	register()
