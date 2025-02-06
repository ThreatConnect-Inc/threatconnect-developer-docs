====================
Indicator Enrichment
====================

Enriching threat intelligence data helps remove false positives and delivers actionable intelligence for threat investigations and other security operations. ThreatConnect includes built-in enrichment services that you can use to retrieve data from a third-party enrichment service that a System Administrator has enabled on your instance and for a given Indicator type.

.. note::
    You must include the following Content-Type HTTP header in your request in order to enrich an Indicator: ``Content-Type: application/json``

Enrich Indicators With Data From an Enrichment Service
------------------------------------------------------

You can use the v3 API to enrich Indicators with data retrieved from the following third-party enrichment services:

- AbuseIPDB
- DomainTools®
- Shodan®
- urlscan.io
- VirusTotal™

.. attention::
    As of ThreatConnect 7.8.1,the RiskIQ® built-in enrichment service is no longer available, because Microsoft® has discontinued the RiskIQ Community Edition.

To enrich Indicators using the v3 API, you must use the ``type`` query parameter in your request and specify which enrichment service(s) to use. See the following table for a list of accepted values for the ``type`` query parameter.

.. attention::

    The accepted values for the ``type`` query parameter are case sensitive.

.. list-table::
   :widths: 25 25 50
   :header-rows: 1

   * - Value Name
     - Enrichment Service
     - Notes
   * - ``AbuseIPDB``
     - AbuseIPDB
     - Available for Address Indicators only
   * - ``DomainTools``
     - DomainTools
     - Available for Host Indicators only
   * - ``Shodan``
     - Shodan
     - Available for Address Indicators only
   * - ``URLScan``
     - urlscan.io
     - Available for URL Indicators only
   * - ``VirusTotalV3``
     - VirusTotal
     - Available for Address, File, Host, and URL Indicators only

API requests to enrich an Indicator will use the API key your System Administrator entered when they enabled and configured the specified enrichment service.

.. attention::

    If the API key your System Administrator entered for an enrichment service exceeds the quota limit set by the enrichment vendor, an error message stating so will be returned by the API.

.. note::

    If you enrich an Indicator that exists in multiple owners, each copy of the Indicator will be enriched. However, only a single API request will be sent to the specified enrichment service.

Enrich a Specific Indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to enrich a specific Indicator with data retrieved from the specified enrichment service(s):

.. code::

    POST /v3/indicators/{indicatorId or indicatorSummary}/enrich?type={enrichmentService}
    Content-Type: application/json

.. note::

    If using an Indicator's summary in the request URI and that Indicator exists in multiple owners, use the ``owner`` `query parameter <https://docs.threatconnect.com/en/latest/rest_api/v3/specify_owner.html>`_ to specify which copy of the Indicator to return data for in the response.

Single Enrichment Service
"""""""""""""""""""""""""

In this first example, the request will enrich the **71.6.135.131** Address Indicator in the API user's Organization  with data retrieved from Shodan.

.. code::

    POST /v3/indicators/71.6.135.131/enrich?type=Shodan
    Content-Type: application/json

JSON Response

.. code:: json

    {
        "data": {
            "id": 15,
            "dateAdded": "2022-09-22T11:47:56Z",
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/#/details/indicators/15/overview",
            "type": "Address",
            "lastModified": "2022-09-22T11:47:56Z",
            "summary": "71.6.135.131",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "ip": "71.6.135.131",
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=71.6.135.131&owner=Demo+Organization",
            "enrichment": {
                "data": [
                    {
                        "type": "Shodan",
                        "hostNames": [
                            "soda.census.224.151.228.245",
                            "soda.census.224.64.23.67"
                        ],
                        "domains": [
                            "67.",
                            "245."
                        ],
                        "country": "United States",
                        "city": "San Diego",
                        "isp": "CariNet, Inc.",
                        "asn": "AS10439",
                        "org": "CariNet, Inc.",
                        "openPorts": [
                            {
                                "transport": "tcp",
                                "port": 22,
                                "product": "OpenSSH",
                                "data": "SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.5\nKey type: ssh-rsa\nKey: AAAAB3NzaC1yc2EAAAADAQABAAABAQCjl6EMm/rwCVDPD0bpSJc5HUfbWxgddKI6L+23g3h+kSNK\nAj4qh+RwT5InvQA6Rqkdc7e0fs+tm1MejA6vkV+7ZX7iKnG00tEi+uM7aEmRZl5CU6O2GNfSYgq9\nzOmhY1ZhRi3OaInZnkDBaYFo1KkGIyzc+ulkW8uch2/WwXuCCC7Yp2IzUdv/pgZgssPqJR0e2Nn/\nub87QA3ayw5V5rEQDq2ESpkEiCUhp8RN4wJAUyEsJMWMV80gOb7obykIc/mtkzjsjh6hvVuPhBGZ\n4govHkmFNNx1hDJ/lRajU006SnJmVZiLwN7yLOmw6F6bqo1qd/REngHRyLvgeuXyfkiN\nFingerprint: 89:8e:ba:1c:71:45:32:41:b4:8a:fe:91:85:3b:16:07\n\nKex Algorithms:\n\tcurve25519-sha256\n\tcurve25519-sha256@libssh.org\n\tecdh-sha2-nistp256\n\tecdh-sha2-nistp384\n\tecdh-sha2-nistp521\n\tdiffie-hellman-group-exchange-sha256\n\tdiffie-hellman-group16-sha512\n\tdiffie-hellman-group18-sha512\n\tdiffie-hellman-group14-sha256\n\tdiffie-hellman-group14-sha1\n\nServer Host Key Algorithms:\n\tssh-rsa\n\trsa-sha2-512\n\trsa-sha2-256\n\tecdsa-sha2-nistp256\n\tssh-ed25519\n\nEncryption Algorithms:\n\tchacha20-poly1305@openssh.com\n\taes128-ctr\n\taes192-ctr\n\taes256-ctr\n\taes128-gcm@openssh.com\n\taes256-gcm@openssh.com\n\nMAC Algorithms:\n\tumac-64-etm@openssh.com\n\tumac-128-etm@openssh.com\n\thmac-sha2-256-etm@openssh.com\n\thmac-sha2-512-etm@openssh.com\n\thmac-sha1-etm@openssh.com\n\tumac-64@openssh.com\n\tumac-128@openssh.com\n\thmac-sha2-256\n\thmac-sha2-512\n\thmac-sha1\n\nCompression Algorithms:\n\tnone\n\tzlib@openssh.com\n"
                            },
                            {
                                "transport": "tcp",
                                "port": 9002,
                                "data": "\\xff\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x7f"
                            }
                        ]
                    }
                ]
            }
        },
        "status": "Success"
    }

In this second example, the request will enrich the URL Indicator whose ID is 20 with data retrieved from urlscan.io.

.. code::

    POST /v3/indicators/20/enrich?type=URLScan
    Content-Type: application/json

JSON Response

.. code:: json
    
    {
        "data": {
            "id": 20,
            "dateAdded": "2023-05-31T14:35:51Z",
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/#/details/indicators/20/overview",
            "type": "URL",
            "lastModified": "2023-05-31T14:35:58Z",
            "summary": "http://nemesis.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "text": "http://nemesis.com",
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/url.xhtml?orgid=1&owner=Demo+Organization",
            "enrichment": {
                "data": [
                    {
                        "type": "URLScan",
                        "malicious": false,
                        "maliciousScore": 0,
                        "domain": "www.brandbucket.com",
                        "ip": {
                            "ip": "2606:4700:10::6816:6d8",
                            "country": "US"
                        },
                        "submittedUrl": "http://nemesis.com/",
                        "effectiveUrl": "https://www.brandbucket.com/names/nemesis?source=ext",
                        "contactSummary": {
                            "ipCount": 1,
                            "countryCount": 1,
                            "domainCount": 7,
                            "httpCount": 110
                        }
                    }
                ]
            }
        },
        "status": "Success"
    }

In this third example, the request will enrich the **218.92.0.227** Address Indicator in the API user's Organization with data retrieved from AbuseIPDB.

.. note::

    The amount of report data retrieved from AbuseIPDB will depend on the value your System Administrator entered for the **Maximum Age of Results (days)** setting when they configured the AbuseIPDB enrichment service in ThreatConnect.

.. code::

    POST /v3/indicators/218.92.0.227/enrich?type=AbuseIPDB
    Content-Type: application/json

JSON Response

.. code:: json
    
    {
        "data": {
            "id": 11175668,
            "dateAdded": "2024-12-10T15:00:22Z",
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/#/details/indicators/11175668",
            "type": "Address",
            "lastModified": "2024-12-10T15:00:22Z",
            "summary": "218.92.0.227",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "ip": "218.92.0.227",
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=218.92.0.227&owner=Demo+Organization",
            "enrichment": {
                "data": [
                    {
                        "type": "AbuseIPDB",
                        "confidenceScore": 100,
                        "reportedCount": 26716,
                        "reportedCountDistinct": 420,
                        "lastReported": "2024-12-10T15:00:21Z",
                        "isp": "CHINANET jiangsu province network",
                        "usageType": "Fixed Line ISP",
                        "domainName": "chinatelecom.cn",
                        "country": "China"
                    }
                ]
            }
        },
        "status": "Success"
    }

Multiple Enrichment Services
""""""""""""""""""""""""""""

When enriching a specific Indicator, you can specify multiple enrichment services from which to retrieve data. In this scenario, each enrichment service must be available for the type of Indicator you want to enrich.

In this example, the request will enrich the zeverco.com Host Indicator in the API user's Organization with data retrieved from DomainTools and VirusTotal.

.. code::

    POST /v3/indicators/zeverco.com/enrich?type=DomainTools&type=VirusTotalV3
    Content-Type: application/json

JSON Response

.. code:: json

    {
        "data": {
            "id": 26,
            "dateAdded": "2023-02-14T17:19:59Z",
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/#/details/indicators/26/overview",
            "type": "Host",
            "lastModified": "2023-02-14T17:19:59Z",
            "summary": "zeverco.com",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "hostName": "zeverco.com",
            "dnsActive": true,
            "whoisActive": true,
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/host.xhtml?host=zeverco.com&owner=Demo+Organization ",
            "enrichment": {
                "data": [
                    {
                        "type": "DomainTools",
                        "overallRiskScore": 100,
                        "malwareRiskScore": 58,
                        "phishingRiskScore": 74,
                        "spamRiskScore": 15,
                        "active": false,
                        "registrantOrg": {
                            "value": "Zeverco.com",
                            "count": 1
                        },
                        "registrar": {
                            "value": "ALIBABA.COM SINGAPORE E-COMMERCE PRIVATE LIMITED",
                            "count": 4148634
                        },
                        "ipList": [
                            {
                                "address": {
                                    "value": "47.91.170.222",
                                    "count": 28939535
                                },
                                "asn": [
                                    {
                                        "value": "45102",
                                        "count": 41325718
                                    }
                                ],
                                "countryCode": {
                                    "value": "hk",
                                    "count": 33985940
                                },
                                "isp": {
                                    "value": "Alicloud-hk",
                                    "count": 9022568
                                }
                            }
                        ]
                    },
                    {
                        "type": "VirusTotal",
                        "vtMaliciousCount": 12
                    }
                ]
            }
        },
        "status": "Success"
    }

If one or more enrichment services is not available for the Indicator type included in the request, an error message indicating which enrichment services are not supported for that Indicator type will be returned. For example, the following request attempts to enrich a Host Indicator with data retrieved from Shodan and VirusTotal. Because Shodan is available for Address Indicators only, an error message stating that the Host Indicator cannot be enriched with Shodan is returned. The Indicator is also not enriched with data from VirusTotal.

.. code::

    POST /v3/indicators/zeverco.com/enrich?type=Shodan&type=VirusTotalV3
    Content-Type: application/json

JSON Response

.. code:: json

    {
        "errCode": "0x1001",
        "message": "The Host zeverco.com cannot be enriched with Shodan because the indicator type isn't supported.",
        "status": "Error"
    }

Enrich Multiple Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^

Send a request in the following format to enrich multiple Indicators with data retrieved from the specified enrichment service(s). Note that the specified enrichment service(s) must be available for each type of Indicator included in the request body.

.. code::

    POST /v3/indicators/enrich?type={enrichmentService}
    Content-Type: application/json
    
    {
        "data": [
            {
                "id": <indicatorId>
            },
            {
                "type": "<indicatorType>",
                "summary": "<indicatorSummary>",
                "ownerName": "<ownerName>"
            },
            {...}
        ]
    }

.. note::

    When using an Indicator's type and summary instead of its ID, you only need to include the ``owner`` field in the request body if the Indicator does not exist in your Organization.

.. attention::

    By default, the maximum number of Indicators that can be enriched in a single request is 500. To adjust this limit, contact your System Administrator.

Single Enrichment Service
"""""""""""""""""""""""""

In the following example, the request will enrich the Indicator whose ID is 15 (i.e., the **71.6.135.131** Address Indicator) and the **evil.com** Host Indicator in one of the API user's Communities with data retrieved from VirusTotal.

.. code::

    POST /v3/indicators/enrich?type=VirusTotalV3
    Content-Type: application/json

    {
        "data": [
            {
                "id": 15
            },
            {
                "type": "Host",
                "summary": "evil.com",
                "ownerName": "Demo Community"
            }
        ]
    }

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 15,
                "dateAdded": "2022-09-22T11:47:56Z",
                "ownerId": 1,
                "ownerName": "Demo Organization",
                "webLink": "https://app.threatconnect.com/#/details/indicators/15/overview",
                "type": "Address",
                "lastModified": "2022-09-22T11:47:56Z",
                "summary": "71.6.135.131",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "ip": "71.6.135.131",
                "legacyLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=71.6.135.131&owner=Demo+Organization",
                "enrichment": {
                    "data": [
                        {
                            "type": "VirusTotal",
                            "vtMaliciousCount": 14
                        }
                    ]
                }
            },
            {
                "id": 22,
                "dateAdded": "2023-03-20T14:40:04Z",
                "ownerId": 2,
                "ownerName": "Demo Community",
                "webLink": "https://app.threatconnect.com/#/details/indicators/22/overview",
                "type": "Host",
                "lastModified": "2023-03-20T14:40:04Z",
                "summary": "evil.com",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "hostName": "evil.com",
                "dnsActive": false,
                "whoisActive": false,
                "legacyLink": "https://app.threatconnect.comauth/indicators/details/host.xhtml?host=evil.com&owner=Demo+Community",
                "enrichment": {
                    "data": [
                        {
                            "type": "VirusTotal",
                            "vtMaliciousCount": 4
                        }
                    ]
                }
            }
        ],
        "enriched": 2,
        "status": "Success"
    }

Multiple Enrichment Services
""""""""""""""""""""""""""""

When enriching multiple Indicators, you can specify multiple enrichment services from which to retrieve data. In this scenario, each enrichment service must be available for the type(s) of Indicator(s) you want to enrich.

In the following example, the request will enrich two Address Indicators in the API user's Organization with data retrieved from Shodan and VirusTotal.

.. code::

    POST /v3/indicators/enrich?type=Shodan&type=VirusTotalV3
    Content-Type: application/json

    {
        "data": [
            {
                "type": "Address",
                "summary": "71.6.135.131"
            },
            {
                "type": "Address",
                "summary": "13.56.33.8"
            }
        ]
    }

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 15,
                "dateAdded": "2022-09-22T11:47:56Z",
                "ownerId": 1,
                "ownerName": "Demo Organization",
                "webLink": "https://app.threatconnect.com/#/details/indicators/15/overview",
                "type": "Address",
                "lastModified": "2022-09-22T11:47:56Z",
                "summary": "71.6.135.131",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "ip": "71.6.135.131",
                "legacyLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=71.6.135.131&owner=Demo+Organization",
                "enrichment": {
                    "data": [
                        {
                            "type": "Shodan",
                            "hostNames": [
                                "soda.census.224.151.228.245",
                                "soda.census.224.64.23.67"
                            ],
                            "domains": [
                                "67.",
                                "245."
                            ],
                            "country": "United States",
                            "city": "San Diego",
                            "isp": "CariNet, Inc.",
                            "asn": "AS10439",
                            "org": "CariNet, Inc.",
                            "openPorts": [
                                {
                                    "transport": "tcp",
                                    "port": 22,
                                    "product": "OpenSSH",
                                    "data": "SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.5\nKey type: ssh-rsa\nKey: AAAAB3NzaC1yc2EAAAADAQABAAABAQCjl6EMm/rwCVDPD0bpSJc5HUfbWxgddKI6L+23g3h+kSNK\nAj4qh+RwT5InvQA6Rqkdc7e0fs+tm1MejA6vkV+7ZX7iKnG00tEi+uM7aEmRZl5CU6O2GNfSYgq9\nzOmhY1ZhRi3OaInZnkDBaYFo1KkGIyzc+ulkW8uch2/WwXuCCC7Yp2IzUdv/pgZgssPqJR0e2Nn/\nub87QA3ayw5V5rEQDq2ESpkEiCUhp8RN4wJAUyEsJMWMV80gOb7obykIc/mtkzjsjh6hvVuPhBGZ\n4govHkmFNNx1hDJ/lRajU006SnJmVZiLwN7yLOmw6F6bqo1qd/REngHRyLvgeuXyfkiN\nFingerprint: 89:8e:ba:1c:71:45:32:41:b4:8a:fe:91:85:3b:16:07\n\nKex Algorithms:\n\tcurve25519-sha256\n\tcurve25519-sha256@libssh.org\n\tecdh-sha2-nistp256\n\tecdh-sha2-nistp384\n\tecdh-sha2-nistp521\n\tdiffie-hellman-group-exchange-sha256\n\tdiffie-hellman-group16-sha512\n\tdiffie-hellman-group18-sha512\n\tdiffie-hellman-group14-sha256\n\tdiffie-hellman-group14-sha1\n\nServer Host Key Algorithms:\n\tssh-rsa\n\trsa-sha2-512\n\trsa-sha2-256\n\tecdsa-sha2-nistp256\n\tssh-ed25519\n\nEncryption Algorithms:\n\tchacha20-poly1305@openssh.com\n\taes128-ctr\n\taes192-ctr\n\taes256-ctr\n\taes128-gcm@openssh.com\n\taes256-gcm@openssh.com\n\nMAC Algorithms:\n\tumac-64-etm@openssh.com\n\tumac-128-etm@openssh.com\n\thmac-sha2-256-etm@openssh.com\n\thmac-sha2-512-etm@openssh.com\n\thmac-sha1-etm@openssh.com\n\tumac-64@openssh.com\n\tumac-128@openssh.com\n\thmac-sha2-256\n\thmac-sha2-512\n\thmac-sha1\n\nCompression Algorithms:\n\tnone\n\tzlib@openssh.com\n"
                                },
                                {
                                    "transport": "tcp",
                                    "port": 9002,
                                    "data": "\\xff\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x7f"
                                }
                            ]
                        },
                        {
                            "type": "VirusTotal",
                            "vtMaliciousCount": 14
                        }
                    ]
                }
            },
            {
                "id": 28,
                "dateAdded": "2023-03-16T16:07:29Z",
                "ownerId": 1,
                "ownerName": "Demo Organization",
                "webLink": "https://app.threatconnect.com/#/details/indicators/28/overview",
                "type": "Address",
                "lastModified": "2023-06-27T15:38:38Z",
                "confidence": 0,
                "source": "Imported from FarSight Passive DNS",
                "summary": "13.56.33.8",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "ip": "13.56.33.8",
                "legacyLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=13.56.33.8&owner=Demo+Organization",
                "enrichment": {
                    "data": [
                        {
                            "type": "Shodan",
                            "hostNames": [
                                "ec2-13-56-33-8.us-west-1.compute.amazonaws.com"
                            ],
                            "domains": [
                                "amazonaws.com"
                            ],
                            "tags": [
                                "self-signed",
                                "cloud"
                            ],
                            "cloudProvider": "Amazon",
                            "cloudRegion": "us-west-1",
                            "country": "United States",
                            "city": "San Jose",
                            "isp": "Amazon.com, Inc.",
                            "asn": "AS16509",
                            "org": "Amazon Technologies Inc.",
                            "openPorts": [
                                {
                                    "transport": "tcp",
                                    "port": 22,
                                    "product": "OpenSSH",
                                    "data": "SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.5\nKey type: ssh-rsa\nKey: AAAAB3NzaC1yc2EAAAADAQABAAABAQDe8kN0qMLv5lPmvNqbDDrhGRPRau3q8Cl9WmmHRsO0fpk+\nqUu4TbZOAA94e8BW7ye/rwQ/2wSpUwtT83bM1EYxacQZ6v1za1R1H5qFC63Ln3X0oflKl8gFXRXl\n+Tyw8X8sqFgPrfvHCdEpB2W4VmXugHtfhnd9KXQB55hLFFf579XRcu4T29d1ndtEshwNS6u/3rMi\nMaDdRRW/8QZC+Qv83QyLhOkx1ru2KZn6ozli0nxBgXKPUSLRQt6pXiYy4p5IRhOIzmDVdllhsNaG\nxgIBMO9abCZhhzNUeNha0MxLwLAS6+2x0bq1N1ri3CFhmANfDNbz3G6qA5dTEy3Hd9ED\nFingerprint: bc:e8:25:20:c7:93:7b:0a:1d:cc:54:92:26:17:e8:f4\n\nKex Algorithms:\n\tcurve25519-sha256\n\tcurve25519-sha256@libssh.org\n\tecdh-sha2-nistp256\n\tecdh-sha2-nistp384\n\tecdh-sha2-nistp521\n\tdiffie-hellman-group-exchange-sha256\n\tdiffie-hellman-group16-sha512\n\tdiffie-hellman-group18-sha512\n\tdiffie-hellman-group14-sha256\n\tdiffie-hellman-group14-sha1\n\nServer Host Key Algorithms:\n\tssh-rsa\n\trsa-sha2-512\n\trsa-sha2-256\n\tecdsa-sha2-nistp256\n\tssh-ed25519\n\nEncryption Algorithms:\n\tchacha20-poly1305@openssh.com\n\taes128-ctr\n\taes192-ctr\n\taes256-ctr\n\taes128-gcm@openssh.com\n\taes256-gcm@openssh.com\n\nMAC Algorithms:\n\tumac-64-etm@openssh.com\n\tumac-128-etm@openssh.com\n\thmac-sha2-256-etm@openssh.com\n\thmac-sha2-512-etm@openssh.com\n\thmac-sha1-etm@openssh.com\n\tumac-64@openssh.com\n\tumac-128@openssh.com\n\thmac-sha2-256\n\thmac-sha2-512\n\thmac-sha1\n\nCompression Algorithms:\n\tnone\n\tzlib@openssh.com\n"
                                },
                                {
                                    "transport": "tcp",
                                    "port": 80,
                                    "product": "OpenResty",
                                    "data": "HTTP/1.1 301 Moved Permanently\r\nServer: openresty/1.15.8.2\r\nDate: Fri, 22 Sep 2023 02:25:08 GMT\r\nContent-Type: text/html\r\nContent-Length: 175\r\nConnection: keep-alive\r\nReferrer-Policy: no-referrer\r\nLocation: https://www.brandbucket.com/names/veraseek?source=ext\r\n\r\n"
                                },
                                {
                                    "transport": "tcp",
                                    "port": 443,
                                    "product": "OpenResty",
                                    "data": "HTTP/1.1 301 Moved Permanently\r\nServer: openresty/1.15.8.2\r\nDate: Fri, 22 Sep 2023 13:19:52 GMT\r\nContent-Type: text/html; charset=UTF-8\r\nTransfer-Encoding: chunked\r\nConnection: keep-alive\r\nLocation: https://www.\r\nRedirect-loc: 0\r\n\r\n",
                                    "ssl": {
                                        "issuer": "sni-support-required-for-valid-ssl",
                                        "subject": "sni-support-required-for-valid-ssl",
                                        "issued": "2019-12-04T08:12:36Z",
                                        "expires": "2029-12-01T08:12:36Z"
                                    }
                                }
                            ]
                        },
                        {
                            "type": "VirusTotal",
                            "vtMaliciousCount": 0
                        }
                    ]
                }
            }
        ],
        "enriched": 2,
        "status": "Success"
    }

If one or more enrichment services is not available for one of the Indicator types included in the request body, then the request will enrich the Indicator types for which the specified enrichment service is available and return a message indicating which Indicators types could not be enriched with that service. For example, the following request attempts to enrich an Address and Host Indicator in the API user's Organization with data retrieved from Shodan and VirusTotal. Because Shodan is available for Address Indicators only, the API response includes a message stating that the Host Indicator cannot be enriched with Shodan.

.. code::

    POST /v3/indicators/enrich?type=Shodan&type=VirusTotalV3
    Content-Type: application/json
    
    {
        "data": [
            {
                "type": "Address",
                "summary": "71.6.135.131"
            },
            {
                "type": "Host",
                "summary": "nemesis.com"
            }
        ]
    }

JSON Response

.. code:: json

    {
        "data": [
            {
                "id": 15,
                "dateAdded": "2022-09-22T11:47:56Z",
                "ownerId": 1,
                "ownerName": "Demo Organization",
                "webLink": "https://app.threatconnect.com/#/details/indicators/15/overview",
                "type": "Address",
                "lastModified": "2022-09-22T11:47:56Z",
                "summary": "71.6.135.131",
                "privateFlag": false,
                "active": true,
                "activeLocked": false,
                "ip": "71.6.135.131",
                "legacyLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=71.6.135.131&owner=Demo+Organization",
                "enrichment": {
                    "data": [
                        {
                            "type": "Shodan",
                            "hostNames": [
                                "soda.census.224.151.228.245",
                                "soda.census.224.64.23.67"
                            ],
                            "domains": [
                                "67.",
                                "245."
                            ],
                            "country": "United States",
                            "city": "San Diego",
                            "isp": "CariNet, Inc.",
                            "asn": "AS10439",
                            "org": "CariNet, Inc.",
                            "openPorts": [
                                {
                                    "transport": "tcp",
                                    "port": 22,
                                    "product": "OpenSSH",
                                    "data": "SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.5\nKey type: ssh-rsa\nKey: AAAAB3NzaC1yc2EAAAADAQABAAABAQCjl6EMm/rwCVDPD0bpSJc5HUfbWxgddKI6L+23g3h+kSNK\nAj4qh+RwT5InvQA6Rqkdc7e0fs+tm1MejA6vkV+7ZX7iKnG00tEi+uM7aEmRZl5CU6O2GNfSYgq9\nzOmhY1ZhRi3OaInZnkDBaYFo1KkGIyzc+ulkW8uch2/WwXuCCC7Yp2IzUdv/pgZgssPqJR0e2Nn/\nub87QA3ayw5V5rEQDq2ESpkEiCUhp8RN4wJAUyEsJMWMV80gOb7obykIc/mtkzjsjh6hvVuPhBGZ\n4govHkmFNNx1hDJ/lRajU006SnJmVZiLwN7yLOmw6F6bqo1qd/REngHRyLvgeuXyfkiN\nFingerprint: 89:8e:ba:1c:71:45:32:41:b4:8a:fe:91:85:3b:16:07\n\nKex Algorithms:\n\tcurve25519-sha256\n\tcurve25519-sha256@libssh.org\n\tecdh-sha2-nistp256\n\tecdh-sha2-nistp384\n\tecdh-sha2-nistp521\n\tdiffie-hellman-group-exchange-sha256\n\tdiffie-hellman-group16-sha512\n\tdiffie-hellman-group18-sha512\n\tdiffie-hellman-group14-sha256\n\tdiffie-hellman-group14-sha1\n\nServer Host Key Algorithms:\n\tssh-rsa\n\trsa-sha2-512\n\trsa-sha2-256\n\tecdsa-sha2-nistp256\n\tssh-ed25519\n\nEncryption Algorithms:\n\tchacha20-poly1305@openssh.com\n\taes128-ctr\n\taes192-ctr\n\taes256-ctr\n\taes128-gcm@openssh.com\n\taes256-gcm@openssh.com\n\nMAC Algorithms:\n\tumac-64-etm@openssh.com\n\tumac-128-etm@openssh.com\n\thmac-sha2-256-etm@openssh.com\n\thmac-sha2-512-etm@openssh.com\n\thmac-sha1-etm@openssh.com\n\tumac-64@openssh.com\n\tumac-128@openssh.com\n\thmac-sha2-256\n\thmac-sha2-512\n\thmac-sha1\n\nCompression Algorithms:\n\tnone\n\tzlib@openssh.com\n"
                                },
                                {
                                    "transport": "tcp",
                                    "port": 9002,
                                    "data": "\\xff\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x7f"
                                }
                            ]
                        },
                        {
                            "type": "VirusTotal",
                            "vtMaliciousCount": 14
                        }
                    ]
                }
            }
        ],
        "enriched": 1,
        "unableEnrich": 1,
        "messages": [
            "[idx=1] nemesis.com: The Host nemesis.com cannot be enriched with Shodan because the indicator type isn't supported."
        ],
        "status": "Success"
    }

Include Enrichment Data in API Responses
----------------------------------------

When using the ``/v3/indicators`` endpoint to create, retrieve, or update Indicators, you can use the ``fields`` `query parameter <https://docs.threatconnect.com/en/latest/rest_api/v3/additional_fields.html>`_ to include the ``enrichment`` field in API responses.

Send a request in the following format to retrieve data for all Indicators or a specific one and include enrichment data for the Indicator(s) in the API response:

Request (All Indicators)

.. code::

    GET /v3/indicators?fields=enrichment

Request (Specific Indicator)

.. code::

    GET /v3/indicators/{indicatorId or indicatorSummary}?fields=enrichment

.. attention::

    You must first enrich an Indicator with a supported enrichment service for data to be populated in the ``enrichment`` field included in the API response.

For example, the following request will retrieve data for the **71.6.135.131** Address Indicator in the API user's Organization and include enrichment data for the Indicator in the API response:

.. code::

    GET /v3/indicators/71.6.135.131?fields=enrichment

JSON Response

.. code:: json

    {
        "data": {
            "id": 15,
            "dateAdded": "2022-09-22T11:47:56Z",
            "ownerId": 1,
            "ownerName": "Demo Organization",
            "webLink": "https://app.threatconnect.com/#/details/indicators/15/overview",
            "type": "Address",
            "lastModified": "2022-09-22T11:47:56Z",
            "summary": "71.6.135.131",
            "privateFlag": false,
            "active": true,
            "activeLocked": false,
            "ip": "71.6.135.131",
            "legacyLink": "https://app.threatconnect.com/auth/indicators/details/address.xhtml?address=71.6.135.131&owner=Demo+Organization",
            "enrichment": {
                "data": [
                    {
                        "type": "VirusTotal",
                        "vtMaliciousCount": 14
                    },
                    {
                        "type": "Shodan",
                        "hostNames": [
                            "soda.census.224.151.228.245",
                            "soda.census.224.64.23.67"
                        ],
                        "domains": [
                            "67.",
                            "245."
                        ],
                        "country": "United States",
                        "city": "San Diego",
                        "isp": "CariNet, Inc.",
                        "asn": "AS10439",
                        "org": "CariNet, Inc.",
                        "openPorts": [
                            {
                                "transport": "tcp",
                                "port": 22,
                                "product": "OpenSSH",
                                "data": "SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.5\nKey type: ssh-rsa\nKey: AAAAB3NzaC1yc2EAAAADAQABAAABAQCjl6EMm/rwCVDPD0bpSJc5HUfbWxgddKI6L+23g3h+kSNK\nAj4qh+RwT5InvQA6Rqkdc7e0fs+tm1MejA6vkV+7ZX7iKnG00tEi+uM7aEmRZl5CU6O2GNfSYgq9\nzOmhY1ZhRi3OaInZnkDBaYFo1KkGIyzc+ulkW8uch2/WwXuCCC7Yp2IzUdv/pgZgssPqJR0e2Nn/\nub87QA3ayw5V5rEQDq2ESpkEiCUhp8RN4wJAUyEsJMWMV80gOb7obykIc/mtkzjsjh6hvVuPhBGZ\n4govHkmFNNx1hDJ/lRajU006SnJmVZiLwN7yLOmw6F6bqo1qd/REngHRyLvgeuXyfkiN\nFingerprint: 89:8e:ba:1c:71:45:32:41:b4:8a:fe:91:85:3b:16:07\n\nKex Algorithms:\n\tcurve25519-sha256\n\tcurve25519-sha256@libssh.org\n\tecdh-sha2-nistp256\n\tecdh-sha2-nistp384\n\tecdh-sha2-nistp521\n\tdiffie-hellman-group-exchange-sha256\n\tdiffie-hellman-group16-sha512\n\tdiffie-hellman-group18-sha512\n\tdiffie-hellman-group14-sha256\n\tdiffie-hellman-group14-sha1\n\nServer Host Key Algorithms:\n\tssh-rsa\n\trsa-sha2-512\n\trsa-sha2-256\n\tecdsa-sha2-nistp256\n\tssh-ed25519\n\nEncryption Algorithms:\n\tchacha20-poly1305@openssh.com\n\taes128-ctr\n\taes192-ctr\n\taes256-ctr\n\taes128-gcm@openssh.com\n\taes256-gcm@openssh.com\n\nMAC Algorithms:\n\tumac-64-etm@openssh.com\n\tumac-128-etm@openssh.com\n\thmac-sha2-256-etm@openssh.com\n\thmac-sha2-512-etm@openssh.com\n\thmac-sha1-etm@openssh.com\n\tumac-64@openssh.com\n\tumac-128@openssh.com\n\thmac-sha2-256\n\thmac-sha2-512\n\thmac-sha1\n\nCompression Algorithms:\n\tnone\n\tzlib@openssh.com\n"
                            },
                            {
                                "transport": "tcp",
                                "port": 9002,
                                "data": "\\xff\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x01\\x7f"
                            }
                        ]
                    }
                ]
            }
        },
        "status": "Success"
    }

----

*DomainTools® is a registered trademark of DomainTools, LLC.*

*RiskIQ® is a registered trademark of Microsoft Corporation.*

*Shodan® is a registered trademark of Shodan.*

*VirusTotal™ is a trademark of Google, Inc.*