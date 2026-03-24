"""
Add a) and b) panel labels to Figure 12 (collaborator-produced).
Overlays bold Arial labels on the existing image.
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

plt.rcParams.update({
    'font.family': 'Arial',
    'figure.dpi': 300,
})

img = mpimg.imread('../figures_to_edit/Figure 12.tiff')
h, w = img.shape[:2]

fig, ax = plt.subplots(figsize=(w / 300, h / 300), dpi=300)
ax.imshow(img)
ax.axis('off')

# Place descriptive labels at top of each panel
# Left panel starts at ~x=0.02, right panel starts at ~x=0.45
ax.text(w * 0.02, h * 0.03, 'a) Flat', fontsize=7, fontweight='bold',
        va='top', ha='left', color='black',
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                  edgecolor='none', alpha=0.8))
ax.text(w * 0.45, h * 0.03, 'b) Income-based', fontsize=7, fontweight='bold',
        va='top', ha='left', color='black',
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                  edgecolor='none', alpha=0.8))

fig.savefig('Figure_12.pdf', dpi=300, bbox_inches='tight', pad_inches=0,
            facecolor='white')
fig.savefig('Figure_12.tiff', dpi=300, bbox_inches='tight', pad_inches=0,
            facecolor='white')
print('Saved: Figure_12.pdf')
print('Saved: Figure_12.tiff')
plt.close()
