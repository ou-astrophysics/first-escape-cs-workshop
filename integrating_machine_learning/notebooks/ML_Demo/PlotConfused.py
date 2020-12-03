import os
import matplotlib.pyplot as mplplot
import pandas as pd
import numpy as np

def makeTitle(prediction, threshold=0.3):
    CATS = prediction.index
    options = prediction > threshold
    order = np.argsort(prediction)[::-1]
    optionStrings = list(
        zip(CATS[order][options[order]], prediction[order][options[order]])
    )

    if len(optionStrings) == 0:
        return "Confused!"

    title = f"$\mathbf{{{optionStrings[0][0]}\ ({optionStrings[0][1]:.2f})}}$"
    if len(optionStrings) > 1:
        return "\n".join(
            [title]
            + [
                ", ".join(
                    [
                        f"{cat} ({prediction:.2f})"
                        for cat, prediction in optionStrings[start : start + 3]
                    ]
                )
                for start in range(1, len(optionStrings), 3)
            ]
        )

    return title


def plotConfusedBatch(image_batch, data_directory):
    borderSize = 90

    f = mplplot.figure(figsize=(30, 20))
    for n, image in enumerate(image_batch.index[:9]):
        subject = mplplot.imread(
            os.path.join(data_directory, f"{image}.jpg")
        )
        canvasBox = (
            slice(borderSize, subject.shape[0] - borderSize - 1),
            slice(borderSize + 50, subject.shape[1] - borderSize - 15),
            slice(None),
        )
        ax = mplplot.subplot(3, 3, n + 1)
        mplplot.imshow(subject[canvasBox])
        mplplot.title(makeTitle(image_batch.iloc[n]), fontsize="xx-large")
        mplplot.axis("off")
    mplplot.tight_layout()
