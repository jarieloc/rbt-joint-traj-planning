import roboticstoolbox as rtb
import numpy as np
from matplotlib import pyplot as plt

panda = rtb.models.DH.Panda()
pandaURDF = rtb.models.Panda()
print(panda)

traj = rtb.jtraj(panda.qz, panda.qr, 100)

pandaURDF.plot(q=traj.q)

fig, ax = plt.subplots(7)
for i in range(7):
    ax[i].plot(traj.q[:, i])
    title = "q" + str(i)
    ax[i].title.set_text(title)
    ax[i].set_xlabel("steps")
    ax[i].set_ylabel("radians")

fig.subplots_adjust(hspace=1.25)
plt.show()
