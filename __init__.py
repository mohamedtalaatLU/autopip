from pip import main as installer
if not hasattr(installer, "main"):
  del pip
  from pip._internal import main as installer
  
if __name__ != "__main__":
  try:
    except ModuleNotFoundError:
      installer(["install", pass])
    
