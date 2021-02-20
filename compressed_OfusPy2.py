#!/usr/bin/env python3
# -*- coding: utf-8 -*-
################################################################################
#
#   OfusPy 2.0.1 - Ofuscador Python
#   Pacheco, Matias W. <mwpacheco@outlook.es>
#   Copyright (c) 2021 Wehaa Portal Soft.
#   License MIT
#
#   WARNING! Do 'NOT' change. You may experience problems with the file.!
#
################################################################################

import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
