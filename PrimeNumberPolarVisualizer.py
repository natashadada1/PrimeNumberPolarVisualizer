"""
Natasha Dada, Fall 2018
Prime Number Visualization

This program graphs the prime numbers in a spiral, represented as distances from the origin (similar to a polar
coordinate system). Using sliders, the user can control how many primes are graphed and the angle between each prime.
This visualization allows us to see several interesting patterns, particularly by manipulating with the angle increment.

The code for the Sliders was adapted from the following example:
https://matplotlib.org/3.1.1/gallery/widgets/slider_demo.html
"""

import math
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


def get_primes(n):
    """
    Using the sieve of Eratosthenes, this function returns a list of prime numbers that are <= n
    :param n: we want all the prime numbers <= n
    :return: list of prime numbers <= n
    """
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if sieve[i] == True:
            j = i*2
            while j <= n:
                sieve[j] = False
                j = j + i
    primes = []
    for i in range(2, n+1):
        if sieve[i] == True:
            primes.append(i)
    return primes


def prime_visualizer():
    """
    Plots the first n prime numbers in polar coordinates, each theta degrees apart. The plot has sliders for n, the
    number of primes, and theta, the angle between each, and a reset button to return to the default values.
    """

    # Make figure
    fig = plt.figure()
    ax = plt.subplot(projection='polar')
    fig.suptitle('Prime Numbers as Distances from the Origin', y=0.97, fontsize=16)
    plt.subplots_adjust(top=0.85, bottom=0.27)

    # Get first 100 primes
    primes = get_primes(542)

    # Default values
    theta_default = 1
    num_primes_default = 50

    # Make sliders
    ax_color = 'lightgoldenrodyellow'
    num_prime_axis = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=ax_color)
    theta_axis = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=ax_color)
    num_prime_slider = Slider(num_prime_axis, 'Number of Primes', 1, 100, valinit=num_primes_default, valstep=1)
    theta_slider = Slider(theta_axis, 'Theta Increment', 0, 360, valinit=theta_default, valstep=1)

    # Update when sliders are changed
    def update(val):
        plt.sca(ax)
        ax.cla()
        theta = theta_slider.val
        num_primes = num_prime_slider.val
        theta_values = [theta * i * math.pi / 180 for i in range(1, num_primes + 1)]
        prime_values = primes[:num_primes]
        plt.plot(theta_values, prime_values, 'ko')

        fig.canvas.draw_idle()

    num_prime_slider.on_changed(update)
    theta_slider.on_changed(update)

    # Reset button
    reset_axis = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(reset_axis, 'Reset', color=ax_color, hovercolor='0.975')

    def reset(event):
        num_prime_slider.reset()
        theta_slider.reset()
    button.on_clicked(reset)

    # Initial plot
    update(None)

    # Show plot
    plt.show()


if __name__ == '__main__':
    prime_visualizer()
