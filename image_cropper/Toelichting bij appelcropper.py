The problem we fixed is in: 
... rembg > sessions > u2net.py
In this .py you will find:

@classmethod
    def download_models(cls, *args, **kwargs):
        fname = f"{cls.name()}.onnx"
        pooch.retrieve(
            "https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx",
            None
            if cls.checksum_disabled(*args, **kwargs)
            else "md5:60024c5c889badc19c04ad937298a77b",
            fname=fname,
            path=cls.u2net_home(*args, **kwargs),
            # progressbar=False,
        ) 
              
Make sure to Comment-out the line that states 'progressbar=False'
