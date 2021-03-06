from fab_phmm.fab_phmm import FABPHMM
import inspect
from experiments.utils import small_model, sample_from_model
import sys


def main():
    """
    PHMM small
    sample from small mode and fit on PHMM
    """
    print(__name__)
    print(inspect.getsource(main))

    smodel = small_model()
    xseqs, yseqs = sample_from_model(smodel, n_samples=200, len_seq=30)

    results = []
    max_nins = 5
    n_same_setting = 3
    for n_xins in range(1, max_nins + 1):
        for n_yins in range(1, max_nins + 1):
            for i in range(1, n_same_setting + 1):
                print("===========")
                print('{} th same setting'.format(i))
                print('training model of ...')
                print('n_xins', n_xins)
                print('n_yins', n_yins)

                fmodel = FABPHMM(n_match_states=1,
                                 n_xins_states=n_xins,
                                 n_yins_states=n_yins,
                                 shrink_threshold=1e-2,
                                 stop_threshold=1e-4,
                                 shrink=False)

                fic = fmodel.fit(xseqs, yseqs, max_iter=500, verbose=True, verbose_level=1)

                result = {}
                result["n_xins"] = n_xins
                result["n_yins"] = n_yins
                result["fic"] = fic
                result["n_hstates"] = fmodel._n_hstates
                result["n_xins"] = n_xins
                result["n_yins"] = n_yins

                results.append(result)

                print("end training with...")
                print(result)

                print()
                sys.stdout.flush()

    results.sort(key=lambda r: - r["fic"])

    print(results)

if __name__ == '__main__':
    main()
