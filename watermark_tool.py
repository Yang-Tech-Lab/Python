"""
Visual Branding Engine: Automated Asset Protection Utility
----------------------------------------------------------
A high-performance imaging utility designed to orchestrate batch 
watermarking sequences with custom transparency and precise positioning.

Author: Yang Jiacheng (Yang-Tech-Lab)
Category: Computer Vision / Automation
Date: February 2026
"""

import logging
from pathlib import Path
from typing import Final, Tuple
from PIL import Image, ImageDraw, ImageFont

# 1. Industrial Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

class ImageBrandingEngine:
    def __init__(self, input_dir: str = "Raw_Assets", output_dir: str = "Branded_Assets"):
        self.input_path = Path(input_dir)
        self.output_path = Path(output_dir)
        self.brand_text: Final[str] = "Designed by Yang-Lab"
        self._initialize_storage()

    def _initialize_storage(self):
        """Ensures the persistence layer (output directory) is provisioned."""
        if not self.output_path.exists():
            self.output_path.mkdir(parents=True)
            logging.info(f"Initialized output repository: {self.output_path}")

    def apply_watermark(self, image_path: Path, opacity: int = 128):
        """
        Synthesizes a branded asset by overlaying a semi-transparent watermark.
        
        :param image_path: Path to the source image.
        :param opacity: Alpha channel value (0-255). 128 for 50% transparency.
        """
        try:
            with Image.open(image_path).convert("RGBA") as base_img:
                # Create a transparent overlay for the watermark
                overlay = Image.new("RGBA", base_img.size, (255, 255, 255, 0))
                draw = ImageDraw.Draw(overlay)
                
                # Dynamic font scaling based on asset dimensions
                font_size = int(base_img.width / 15)
                # Note: For professional use, load a .ttf file using ImageFont.truetype()
                font = ImageFont.load_default() 

                # Precise coordinate calculation for Bottom-Right placement
                bbox = draw.textbbox((0, 0), self.brand_text, font=font)
                text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
                
                margin = 20
                coords = (base_img.width - text_w - margin, base_img.height - text_h - margin)

                # Rendering text with alpha blending (Semi-transparent White)
                draw.text(coords, self.brand_text, font=font, fill=(255, 255, 255, opacity))

                # Composite the overlay onto the original asset
                branded_asset = Image.alpha_composite(base_img, overlay)
                
                # Persist to disk (Convert back to RGB for JPEG compatibility)
                output_file = self.output_path / image_path.name
                branded_asset.convert("RGB").save(output_file, "JPEG", quality=95)
                logging.info(f"Successfully branded: {image_path.name}")

        except Exception as e:
            logging.error(f"Critical failure during asset synthesis for {image_path.name}: {e}")

    def execute_batch_sequence(self):
        """Orchestrates the batch processing lifecycle for all identified assets."""
        valid_extensions = ('.jpg', '.jpeg', '.png')
        assets = [f for f in self.input_path.iterdir() if f.suffix.lower() in valid_extensions]
        
        if not assets:
            logging.warning(f"No valid assets detected in {self.input_path}. Operation aborted.")
            return

        logging.info(f"🚀 Initiating batch branding for {len(assets)} assets...")
        for asset in assets:
            self.apply_watermark(asset)
        
        logging.info("-" * 45)
        logging.info(f"✅ Orchestration Complete. Assets persisted at: [{self.output_path}]")

if __name__ == "__main__":
    # Deployment in Guangzhou Local Environment
    engine = ImageBrandingEngine()
    engine.execute_batch_sequence()
