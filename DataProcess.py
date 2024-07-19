import os
import sys
import bpy

'''
@description: travel the folder and get the file path
@param {string} root_directory the root directory
@param {string} data_directory the data directory
@param {string} output_directory the output directory
'''
def travel_folder(root_directory, data_directory, output_directory):
    for root, dirs, files in os.walk(data_directory):
        # for file in files:
        #     file_path = os.path.join(root, file)
        #     print(file_path)
        if root == data_directory:
            continue
        process(root_directory, root, output_directory)


'''
@description: process the file
@param {string} root_directory the root directory
@param {string} dir_path the process data directory path
@param {string} output_directory the output directory
'''
def process(root_directory,dir_path, output_directory):
    tmp = dir_path.split('\\')
    current_dir_name = tmp[-1]
    output_glb_directory = output_directory + "/" + current_dir_name + "_glb"
    if not os.path.isdir(output_glb_directory):
        os.mkdir(output_glb_directory)
    #ply2glb
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            tmp, file_extension = os.path.splitext(file)
            tmp = tmp.split('/')
            file_name = tmp[-1]
            if file_extension == ".ply":
                bpy.ops.import_mesh.ply(filepath=dir_path+'/'+file)
                export_file = output_glb_directory + "/" + file_name + ".glb"
                bpy.ops.export_scene.gltf(filepath=export_file, export_format='GLB')
                print(1)

    #glb2b3dm
    output_b3dm_directory = output_directory + "/" + current_dir_name + "_b3dm"
    if not os.path.isdir(output_b3dm_directory):
        os.mkdir(output_b3dm_directory)
    for root, dirs, files in os.walk(output_glb_directory):
        for file in files:
            tmp, file_extension = os.path.splitext(file)
            tmp = tmp.split('/')
            file_name = tmp[-1]
            if file_extension == ".glb":
                input_file = output_glb_directory + "/" + file
                output_file = output_b3dm_directory + "/" + file_name + ".b3dm"
                os.system("node " + root_directory + '/3d-tiles-tools/tools/bin/3d-tiles-tools.js glbToB3dm '+ input_file + ' ' + output_file)


if __name__=='__main__':
    bpy.ops.wm.read_factory_settings(use_empty=True)
    # Get the root directory
    root_directory = os.getcwd()
    # Get the data dir path
    force_continue = True
    for current_argument in sys.argv:
        if force_continue:
            if current_argument == '--':
                force_continue = False
            continue

    #check output directory is exist
    if not os.path.isdir(root_directory+"/output"):
        os.mkdir(root_directory+"/output")

    #try:
    # for file in os.listdir(current_argument):
    #     travel_folder(root_directory, current_argument, root_directory+"/output")
    # except Exception as e:
    #     print(e)
    #     print("The file path is not a directory.")
    for file in os.listdir(current_argument):
        travel_folder(root_directory, current_argument, root_directory+"/output")

