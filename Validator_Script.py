import unreal
import math

editor_util = unreal.EditorUtilityLibrary()

# 選択中のアセット取得

selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
not_pow = 0

# 選択されたアセットをループ処理
for asset in selected_assets:
    
    asset_name = asset.get_fname()
    asset_path = asset.get_path_name()

    try :
         # アセットのサイズを取得
        x_size = asset.blueprint_get_size_x()
        y_size = asset.blueprint_get_size_y()

        # サイズが2のべき乗かどうかをチェック
        is_x_valid = math.log(x_size, 2).is_integer()
        is_y_valid = math.log(y_size, 2).is_integer()

        if not is_x_valid or not is_y_valid:
            unreal.log("{} is not power of ({}, {})".format(asset_name, x_size, y_size))
            unreal.log("It's path is {}".format(asset_path))
            not_pow += 1
    
    except Exception as error:
        unreal.log("{} is not a Texture - {}".format(asset_name, error))

unreal.log("{} checked, {} textures found problematic". format(num_assets, not_pow))