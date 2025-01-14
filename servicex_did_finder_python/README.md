<<<<<<< HEAD
<img src="docs/img/ServiceX-Color-ImageOnly-Transparent.png" width="200" height="200">

# ServiceX - Data Delivery for the HEP Community

![Uproot Status](https://github.com/ssl-hep/servicex-backend-tests/actions/workflows/daily_servicex_uproot_test_af.yml/badge.svg) 
![xAOD Status](https://github.com/ssl-hep/servicex-backend-tests/actions/workflows/daily_servicex_xaod_test_af.yml/badge.svg)

ServiceX is an on-demand service that delivers data straight from the grid to high energy physics analysts in an easy, flexible, and highly performant manner.

## Features
- __Experiment-agnostic:__ Supports both the ATLAS and CMS collaborations on the LHC.
- __Custom filters and pre-processing:__ Easily filter events, request specific columns, and unpack compressed formats using the [func-adl](https://github.com/iris-hep/func_adl) analysis description language.
- __Choose your format:__ ServiceX can deliver data in a variety of columnar formats, including streams of ROOT data, small ROOT files, HDF5, and Apache Arrow buffers.
- __No hassle:__ ServiceX uses Rucio to find and access data wherever it lives, so users don't have to worry about these details.
- __Simple and Pythonic:__ Using ServiceX takes only a few lines of code in any Python environment, such as a script  or Jupyter notebook.

## Getting Started

Check out our [quick start guide](https://servicex.readthedocs.io/en/latest/user/getting-started/) 
for instructions on how to obtain credentials, 
install the [ServiceX Python library](https://pypi.org/project/servicex/),
and make your first ServiceX transformation request.

## Documentation

[![Documentation Status](https://readthedocs.org/projects/servicex/badge/?version=latest)](https://servicex.readthedocs.io/en/latest/?badge=latest)

The [ServiceX documentation](https://servicex.readthedocs.io/en/latest/) is hosted on Read the Docs.

## Self-Hosting

The [Scalable Systems Laboratory](https://iris-hep.org/ssl.html) (SSL) at IRIS-HEP maintains multiple instances of ServiceX to transform several input formats from different experiments.

In addition, ServiceX is an open-source project, and you are welcome to host your own deployment. 
Instructions on how to configure and deploy ServiceX can be found in our 
[deployment guide](https://servicex.readthedocs.io/en/latest/deployment/basic/).

## Contributing

The ServiceX team welcomes community contributions. If you'd like to get involved, please check out our 
[contributor guide](https://servicex.readthedocs.io/en/latest/development/contributing/).

## License

ServiceX is distributed under a [BSD 3-Clause License](LICENSE).

## Acknowledgements
![](https://iris-hep.org/assets/logos/Iris-hep-5-just-graphic.png)
![](https://iris-hep.org/assets/images/nsf-logo-128.png)

ServiceX is a component of the [IRIS-HEP](https://iris-hep.org/) Intelligent Data Delivery Service, and is supported by National Science Foundation under [Cooperative 
Agreement OAC-1836650](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1836650). Any opinions, findings, conclusions or recommendations 
expressed in this material are those of the authors and do not necessarily 
reflect the views of the National Science Foundation.
=======
# ServiceX_Code_Generator_Python

This code generator takes python code/function and passes it unmodified for use by the transformer.

For instance, the following python function was saved in the file selection.py:

```
def transform_yt(ds):
    slc = ds.r[ds.domain_center[0], :, :].plot(("gas", "density"))
    sac = slc.frb[("gas", "density")].d
    return sac
```

The json passed to the transformer will need this function base64 encoded. To encode your python code:

```
cat selection.py | base64
```

Then in the json the "selection" key will take the base64-encoded string:
``` 
selection: "ZGVmIHRyYW5zZm9ybV95dChkcyk6CiAgICBzbGMgPSBkcy5yW2RzLmRvbWFpbl9jZW50ZXJbMF0sIDosIDpdLnBsb3QoKCJnYXMiLCAiZGVuc2l0eSIpKQogICAgc2FjID0gc2xjLmZyYlsoImdhcyIsICJkZW5zaXR5IildLmQKICAgIHJldHVybiBzYWMK"
```

Here is an example using the [ServiceX frontend](https://github.com/ssl-hep/ServiceX_frontend):

```
from servicex import ServiceXDataset
from servicex.servicex_python_function import ServiceXPythonFunction

def transform_yt(ds):
    slc = ds.r[ds.domain_center[0], :, :].plot(("gas", "density"))
    sac = slc.frb[("gas", "density")].d
    return sac

if __name__ == "__main__":
    dataset = "girder://579fb0aa7b6f0800011ea3b6#item"
    
    ds = ServiceXDataset(dataset, 
                         backend_name = "python"
    )
    selection = ServiceXPythonFunction(ds)
    encoded_selection = selection._encode_function(transform_yt)
    r = ds.get_data_pandas_df(encoded_selection)
    print(r)
```
>>>>>>> prajwal-test-gha
