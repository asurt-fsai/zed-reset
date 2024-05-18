import pyzed.sl as sl

def reset_zed_camera():
    zed = sl.Camera()

    init_params = sl.InitParameters()

    status = zed.open(init_params)
    if status != sl.ERROR_CODE.SUCCESS:
        print(f"Error opening ZED camera: {status}")
        return
    
    zed.close()
    status = zed.open(init_params)
    if status == sl.ERROR_CODE.SUCCESS:
        print("Zed camera restarted succesfully")
    else:
        print(f"Error restarting ZED camera: {status}")

    zed.close()

reset_zed_camera()