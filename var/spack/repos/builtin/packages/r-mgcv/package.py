# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RMgcv(RPackage):
    """GAMs, GAMMs and other generalized ridge regression with multiple
    smoothing parameter estimation by GCV, REML or UBRE/AIC. Includes a gam()
    function, a wide variety of smoothers, JAGS support and distributions
    beyond the exponential family."""

    homepage = "https://cran.r-project.org/package=mgcv"
    url      = "https://cran.r-project.org/src/contrib/mgcv_1.8-16.tar.gz"
    list_url = "https://cran.r-project.org/src/contrib/Archive/mgcv"

    version('1.8-22', 'b42079b33b46de784f293a74c824b877')
    version('1.8-21', 'aae8262a07c8698ca8d6213065c4983f')
    version('1.8-20', '58eb94404aad7ff8a0cf11a2f098f8bf')
    version('1.8-19', 'f9a4e29464f4d10b7b2cb9d0bec3fa9e')
    version('1.8-18', 'c134fc2db253530233b95f2e36b56a2f')
    version('1.8-17', '398582d0f999ac34749f4f5f1d103f75')
    version('1.8-16', '4c1d85e0f80b017bccb4b63395842911')
    version('1.8-13', '30607be3aaf44b13bd8c81fc32e8c984')

    depends_on('r-nlme', type=('build', 'run'))
    depends_on('r-matrix', type=('build', 'run'))
