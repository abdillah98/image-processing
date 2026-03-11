import sys

from src.experiments import exp_blur, exp_histogram

experiments = {
    "histogram": exp_histogram.run,
    "blur": exp_blur.run
}

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Available experiments:")
        for k in experiments:
            print("-", k)
        exit()

    exp_name = sys.argv[1]

    if exp_name in experiments:
        experiments[exp_name]()
    else:
        print("Experiment not found")