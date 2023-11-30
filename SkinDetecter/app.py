from src.skinDetector import SkinDetector
imageName = 'D:\workspace\DA Python XLA\Image\Training_1.jpg'
detector = SkinDetector(image_path = imageName)
detector.find_skin()
detector.show_all_images()