import pip as installer
if not hasattr(pip, "main"):
  del installer
  import pip._internal as installer
  
if __name__ != "__main__":
  try:
    except ModuleNotFoundError:
      installer.main(["install", pass])
    
else :
  print("this module is for external usage only !")
    
