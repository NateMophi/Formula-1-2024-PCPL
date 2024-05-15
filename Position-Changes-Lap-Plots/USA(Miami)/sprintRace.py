import fastf1.plotting
import fastf1 as ff1
import matplotlib.pyplot as plt

ff1.Cache.enable_cache("cache")
fastf1.plotting.setup_mpl(misc_mpl_mods=False)
fig, ax = plt.subplots(figsize=(8,4.9))

session = ff1.get_session(2024, 6, "R")
session.load(telemetry=False, weather=False)

for drv in session.drivers:
    drv_laps = session.laps.pick_driver(drv)
    abb = drv_laps["Driver"].iloc[0]
    color = fastf1.plotting.driver_color(abb)
    ax.plot(drv_laps["LapNumber"], drv_laps['Position'], label=abb, color=color)

ax.set_ylim([20.5,0.5])
ax.set_yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
ax.set_xlabel("Lap")
ax.set_ylabel("Position")
ax.legend(bbox_to_anchor=(1.0, 1.02))
plt.tight_layout()
plt.show()
