import math

def calc_offset_3d(elev_deg, azim_deg, screen_dx, screen_dy):
    theta = math.radians(elev_deg)
    phi = math.radians(azim_deg)

    # Simplified approximation to convert screen offset to 3D offset
    # We ignore dz for horizontal arrows (B-C, C-D)
    dx = screen_dx * math.cos(phi) - screen_dy * math.sin(phi) * math.sin(theta)
    dy = screen_dx * math.sin(phi) + screen_dy * math.cos(phi) * math.sin(theta)
    dz = screen_dy * math.cos(theta)

    return dx, dy, dz

# Example: take your first prism, B-C arrow ~ (0,0.8,0)
elev_azim = [(30,110), (80,110), (30,160), (80,160)]
desired_screen_offsets = [
    (0,0.8),  # B-C
    (0,1.4),
    (0,0.6),
    (0,2.0)
]

for (theta, phi), (sx, sy) in zip(elev_azim, desired_screen_offsets):
    dx, dy, dz = calc_offset_3d(theta, phi, sx, sy)
    print(f"Elev {theta}, Azim {phi}: 3D offset ~ ({dx:.2f}, {dy:.2f}, {dz:.2f})")
