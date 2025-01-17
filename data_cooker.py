import numpy as np
import matplotlib.pyplot as plt


def create_synthetic_data(lines, title):

    # Generate synthetic data
    wavelengths = np.linspace(380, 700, 1000)
    emission_spectrum = np.zeros_like(wavelengths)
    absorption_spectrum = np.ones_like(wavelengths)
    

    # Gaussian profiles for the lines
    for line, intensity in lines:
        noise = np.random.normal(0, 0.01, wavelengths.shape)
        emission_spectrum += intensity * np.exp(-0.5 * ((wavelengths - line) / 1.0)**2)
        emission_spectrum += noise

        # different noise for more realistic effect
        noise = np.random.normal(0, 0.01, wavelengths.shape)
        absorption_spectrum -= intensity * 0.5 * np.exp(-0.5 * ((wavelengths - line) / 1.0)**2)
        absorption_spectrum += noise



    # Plot the data
    plt.figure(figsize=(14, 8))

    plt.subplot(2, 1, 1)
    plt.plot(wavelengths, absorption_spectrum)
    plt.title('Position A', fontsize=16)
    plt.ylabel('Intensity', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=12)
    plt.ylim(-0.1, 1.2)

    plt.subplot(2, 1, 2)
    plt.plot(wavelengths, emission_spectrum)
    plt.title('Position B', fontsize=16)
    plt.xlabel('Wavelength (nm)', fontsize=14)
    plt.ylabel('Intensity', fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=12)
    plt.ylim(-0.1, 1.2)

    plt.suptitle(title, fontsize=18)
    plt.savefig(title + '.png')
    plt.show()

# Define wavelengths and relative intensities for helium and hydrogen emission and absorption lines
hydrogen_lines = [(410.2, 0.2), (434.0, 0.3), (486.1, 0.8), (656.3, 1.0)]
helium_lines = [(388.9, 0.2), (447.1, 1.1), (501.6, 0.1), (587.6, 1.0), (667.8, 0.4)]
no_sample = [(0, 0)]

if __name__ == '__main__':
    create_synthetic_data(hydrogen_lines, 'Hydrogen')
    create_synthetic_data(helium_lines, 'Helium')
    create_synthetic_data(no_sample, 'No Sample - Control')
    plt.close('all')
