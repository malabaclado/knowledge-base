
Create a virtual environment
```
python3.x -m venv idp
```


Install packages via pip: https://www.intel.com/content/www/us/en/developer/articles/tool/whats-included-distribution-for-python.html



| package     | pip command                                                         |
| ----------- | ------------------------------------------------------------------- |
| numpy       | `pip install -i https://pypi.anaconda.org/intel/simple numpy`       |
| scipy       | `pip install -i https://pypi.anaconda.org/intel/simple scipy`       |
| mkl_service | `pip install -i https://pypi.anaconda.org/intel/simple mkl-service` |
| mkl_fft     | `pip install -i https://pypi.anaconda.org/intel/simple mkl-fft`     |
| mkl_umath   | `pip install -i https://pypi.anaconda.org/intel/simple mkl-umath`   |
| mkl_random  | `pip install -i https://pypi.anaconda.org/intel/simple mkl-random`  |
| dpnp        | `pip install -i https://pypi.anaconda.org/intel/simple dpnp`        |

Remarks
- mkl_service, mkl_fft, mkl_umath, mkl_random - It is not typically necessary to install these package/s with Intel optimized NumPy, SciPy, or NumExpr because they come with this package. However, it may be needed with other Python packages that rely on oneMKL if fine-grain control is necessary.