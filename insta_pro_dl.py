import instaloader
user = input("enter an id : ")
mod = instaloader.Instaloader()
mod.download_profile(user,profile_pic_only=True)