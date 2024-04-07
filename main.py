from avatar_generator import AvatarGenerator
from notifypy import Notify


def generate_avatar():
    generator = AvatarGenerator("./images")
    generator.generate_avatar(100)
    notification = Notify()
    notification.title = "NFT AvatarGenerator"
    notification.message = "Generating NFT Art Styled Avatar Profile Pictures."
    notification.send()



if __name__ == "__main__":
    generate_avatar()
    notification = Notify()
    notification.title = "NFT AvatarGenerator"
    notification.message = "NFT Art Styled Avatar Profile Pictures Generated."
    notification.send()