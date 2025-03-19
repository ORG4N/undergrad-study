/*
 * Google Cloud Certificates
 * Copyright (c) 2019-2020, Arm Limited and affiliates.
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef AZURE_CLOUD_CREDENTIALS_H
#define AZURE_CLOUD_CREDENTIALS_H

namespace azure_cloud {
    namespace credentials {
        /*
        * Primary Connecion String
        */

        // Use https://dpsgen.z8.web.core.windows.net/ to obtain YOUR connection string
        // This one will not work, but I guess you knew that ;)
        const char iothub_connection_string[] = "HostName=iotc-bc7eb0b5-8337-4d7e-abac-cf34ceb1f83d.azure-devices.net;DeviceId=idntg4hc4t;SharedAccessKey=WX3mBL5qvlOcRYPeEopBakyvB1oA8VR2A7FGHU0mgiY=";
    }
}
#endif
