import imageio
import matplotlib.pyplot as plt

# Write your function here!


def main():
    duck = imageio.imread("duck.jpg")
    duck = duckie_hat(duck)
    plt.imshow(duck)
    plt.savefig("duckie_hat.png")


if __name__ == "__main__":
    main()
