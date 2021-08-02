# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-ITSM 蓝鲸流程服务 available.

Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.

BK-ITSM 蓝鲸流程服务 is licensed under the MIT License.

License for BK-ITSM 蓝鲸流程服务:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Generated by Django 1.11.24 on 2019-11-13 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0027_auto_20190919_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='tag',
            field=models.CharField(default='DEFAULT', max_length=255, verbose_name='\u8282\u70b9\u6807\u7b7e'),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(
                choices=[
                    ('WAIT', '\u5f85\u5904\u7406'),
                    ('QUEUEING', '\u540e\u53f0\u5904\u7406\u4e2d'),
                    ('RUNNING', '\u5904\u7406\u4e2d'),
                    ('RECEIVING', '\u5f85\u8ba4\u9886'),
                    ('DISTRIBUTING', '\u5f85\u5206\u6d3e'),
                    ('TERMINATED', '\u88ab\u7ec8\u6b62'),
                    ('FINISHED', '\u5df2\u7ed3\u675f'),
                    ('FAILED', '\u6267\u884c\u5931\u8d25'),
                    ('SUSPEND', '\u88ab\u6302\u8d77'),
                ],
                default='WAIT',
                max_length=32,
                verbose_name='\u8282\u70b9\u72b6\u6001',
            ),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='current_status',
            field=models.CharField(
                choices=[
                    ('RUNNING', '\u5904\u7406\u4e2d'),
                    ('SUSPENDED', '\u6302\u8d77'),
                    ('FINISHED', '\u5df2\u7ed3\u675f'),
                    ('TERMINATED', '\u88ab\u7ec8\u6b62'),
                ],
                default='RUNNING',
                max_length=32,
                verbose_name='\u5355\u636e\u72b6\u6001',
            ),
        ),
    ]