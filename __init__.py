import pip as installer
if not hasattr(installer, "main"):
  del installer
  import pip._internal as installer
  
if __name__ != "__main__":
  try:
    except ModuleNotFoundError:
      installer.main(["install", pass])#This part is not implemented yet
    
else :
  print("this module is for external usage only !")
    
