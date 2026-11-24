import matplotlib.pyplot as plt


def chiz_grafiklar():
    oylar = ["Yan", "Fev", "Mar", "Apr", "May", "Iyun"]
    daromad = [12, 15, 11, 19, 22, 18]

    kategoriyalar = ["Texnika", "Kiyim", "Oziq-ovqat"]
    savdo = [35, 20, 45]

    buyurtma_qiymatlari = [50, 75, 80, 120, 150, 150, 180, 220, 250, 300]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Ma'lumotlar tahlili grafiklari", fontsize=16, fontweight="bold")

    axes[0].plot(oylar, daromad, marker="o", color="blue", linewidth=2, linestyle="-")
    axes[0].set_title("Oylik daromad dinamikasi")
    axes[0].set_xlabel("Oylar")
    axes[0].set_ylabel("Daromad (mln so'm)")
    axes[0].grid(True, linestyle="--", alpha=0.6)

    ranglar = ["#2ecc71", "#e74c3c", "#f39c12"]
    axes[1].bar(kategoriyalar, savdo, color=ranglar, edgecolor="black")
    axes[1].set_title("Kategoriyalar savdosi")
    axes[1].set_xlabel("Kategoriyalar")
    axes[1].set_ylabel("Savdo (dona)")
    axes[1].grid(axis="y", linestyle="--", alpha=0.6)

    axes[2].hist(buyurtma_qiymatlari, bins=5, color="purple", edgecolor="black", alpha=0.7)
    axes[2].set_title("Buyurtma qiymatlari taqsimoti")
    axes[2].set_xlabel("Buyurtma qiymatlari")
    axes[2].set_ylabel("Takrorlanish soni (Chastota)")
    axes[2].grid(axis="y", linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig("grafiklar.png", dpi=300)
    print("Grafiklar muvaffaqiyatli chizildi va 'grafiklar.png' fayliga saqlandi.")

    plt.show()


if __name__ == "__main__":
    chiz_grafiklar()
