"""
Fichier stub pour le module realesrgan
"""

class RealESRGANer:
    def __init__(self, scale, model_path, model, tile, tile_pad, pre_pad, half, device):
        self.scale = scale
        self.model_path = model_path
        self.model = model
        self.tile = tile
        self.tile_pad = tile_pad
        self.pre_pad = pre_pad
        self.half = half
        self.device = device
    
    def enhance(self, img, outscale=None):
        """Stub pour la méthode enhance"""
        return img, None 