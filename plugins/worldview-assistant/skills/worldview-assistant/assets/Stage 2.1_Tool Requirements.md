# **Consolidated Tool Requirements Document**

# **1\. Executive Overview**

This document defines the unified, implementation-ready tool and API requirements for the Stage-1 NASA Worldview Agent.

The agent enables users to:

* Discover NASA datasets  
* Understand variable meaning and caveats  
* Visualize data in NASA Worldview  
* Perform visualization-native statistical analysis  
* Transition to dataset download via Earthdata Search

Scope constraints:

* Public-only datasets  
* Visualization-first architecture  
* Metadata-authoritative (UMM-based)  
* No raw granule retrieval  
* No server-side modeling  
* No predictive analytics

# **2\. Tool Inventory** 

## **2.1 NASA Worldview**

### **Role**

Primary visualization interface and deep-link target.

### **Capabilities**

* Layer rendering  
* Layer comparison (Swipe, Spy, Opacity)  
* Charting mode  
* Time selection  
* Projection switching  
* Deep link configuration

### **Agent Usage Model**

* Generate deep links  
* Mirror UI-supported configuration  
* No direct UI automation

## **2.2 Worldview Parameter URL documentation**

### [**https://github.com/nasa-gibs/worldview/blob/main/doc/url\_parameters.md**](https://github.com/nasa-gibs/worldview/blob/main/doc/url_parameters.md)

| Parameter | Type | Value | Description |
| ----- | ----- | ----- | ----- |
| p | string | geographic, arctic or antarctic | Selected projection. |
| v | string | *minX,minY,maxX,maxY* | Extent of the map viewport in units based on the projection selected (degrees for geographic, meters for others). |
| l (l1 for B state) | string | *layer\_id1,layer\_id2,..,layer\_idN* | Active layer list where layer\_id is the identifier of the layer as defined in the configuration file. Any number of baselayers or overlays may be specified (separated by a ,). |
|  | boolean | *layer\_id(hidden)* | If present, this layer will appear in the layer list but not shown on the map. |
|  | string | *layer\_id(opacity=value)* | If present, assigns an opacity value to a layer where layer\_id is the identifier of the layer, as defined in the configuration file, and value is a real number in the range of 0 to 1 where 0 is fully transparent and 1 is fully opaque. Any number of layer to opacity value mappings may be specified. |
|  | string | *layer\_id(palettes=value1,value2,..,valueN)* | If palettes is present, a custom palette will be assigned to a raster layer where layer\_id is the identifier of the layer and value is the identifier of the palette, as defined in the configuration file. Any number of raster layer to palette mappings may be specified. |
|  | string | *layer\_id(squash)* | If squash is present and a min or max value is set, the palette will start or end at the designated min/max values and the palette will adjust to these bounds. |
|  | string | *layer\_id(min=value1,value2)* | If min is present, the raster layer palettes will start at the defined value. This value can be paired with max and squash to customize the entire palette range. |
|  | string | *layer\_id(max=value1,value2)* | If max is present, the raster layer palettes will end at the defined value. This value can be paired with min and squash to customize the entire palette range. |
|  | string | *layer\_id(style=value)* | If style is present, a custom vector style, will be assigned to a vector layer where layer\_id is the identifier of the layer and value is the identifier of the vector style, as defined in the configuration file. |
| lg (lg1 for B state) | boolean | *true* or *false* | If false, layers are not grouped. If this parameter is absent, it is considered true and layers will be grouped |
| t (t1 for B state) | date | *YYYY-MM-DD-Thh:mm:ssZ* | Selected UTC day and time.\*\* |
| z | number | 1 to 5 | The timescale axis zoom value from 1 to 5.\* |
| i | number | 1 to 5 | The timeline interval value from 1 to 5.\* |
| ics | boolean | *true* or *false* | If custom selected is true, a custom interval and custom delta will be active and allow custom intervals in time changes. |
| ici | number | 1 to 5 | The custom interval value from 1 to 5\* identifies which time unit is changed by the date change arrows and optionally animation. *\*Only active and saved in url if custom selected is true.* |
| icd | number | 1 to 999 | The custom delta value for how many custom interval time units are added or subtracted when using the date change arrows and optionally animation. *\*Only active and saved in url if custom selected is true.* |
| e | string,date | *event\_id,yyyy-mm-dd* | If any value is present, the events tab will be activated. If the value is a valid event\_id, the corresponding event will be highlighted in the event list. If a date (YYYY-MM-DD) is added to the event\_id, then the selected event for the specified date will be shown. |
| efs | boolean | *true* or *false* | Determines whether to "show all" events that match the date range and category filters or, to also include the current map viewport bounding box in the event API call to limit results to that area. Default: true (which means show all; no bbox included) |
| efd | string | yyyy-mm-dd,yyyy-mm-dd | The event start and end dates to be included in an event API request. Default range is last 120 days from current app load time. |
| efc | string | id,id,id | The event category ids for each category to be included in an event API request. |
| s | string | *coordinates* | A pair of coordinates using Decimal Degrees format (DDD.DDDD,DDD.DDDD) to add a Location Search marker onto the map. To add more than one Location Search marker, separate coordinate pairs with a plus symbol. (DDD.DDDD,DDD.DDDD+DDD.DDDD,DDD.DDDD) |
| ab | boolean | on | If set to "on", the animation widget will be shown. |
| aa | boolean | false | If set to "true", the animation will play on load. NOTE: The URL also requires valid animation parameters (ab, av, etc.). |
| as | date | *YYYY-MM-DDThh:mm:ssZ* | The animation start day & time.\*\* |
| ae | date | *YYYY-MM-DDThh:mm:ssZ* | The animation end day & time.\*\* |
| av | number | 1 to 10 | The animation speed value from 1 to 10\. 1 \= slowest, 10 \= fastest. |
| al | boolean | *true* or *false* | If any value is set, the animation loop will be turned on. Animation looping is disabled by default. |
| ca | boolean | *true* or *false* | Determines if the A or B state is active. If this parameter exists at all, compare mode will be active. If ca=true, Compare mode will be active in the A state. |
| cm | string | *swipe* , *spy* or *opacity* | If comparison mode is active (ca=true|false) the cm parameter will determine which comparison mode to use. Default mode is swipe. |
| cv | Number | 0 to 100 | If ca='true|false', The cv parameter is used to determine the location of the swiper or the value of opacity depending on the selected mode. Default is 50 which will place the swiper on the middle of any screen. This parameter is irrelevant when the spy mode is active (cm=spy). |
| cha | boolean | *true* or *false* | If true value is set, charting mode will be active. |
| chl | string | *layer\_id* | Currently selected layer for charting mode, where layer\_id is the identifier of the layer as defined in the configuration file. |
| chc | string | *coordinates* | A pair of coordinates in the format x1,y1,x2,y2 for where the area of interest selection is placed for charting mode. |
| cht | date | *YYYY-MM-DDThh:mm:ssZ* | The charting mode chart start day & time. |
| cht2 | date | *YYYY-MM-DDThh:mm:ssZ* | The charting mode chart end day & time. If not present, but cht is present, charting timespan is considered to be a single date span. |
| chch | boolean | *true* or *false* | If true value is set, charting mode chart will be requested and shown on page load. |
| download | string | *product\_id* | If any value is set, the data download tab will be activated. If a product identifier is set, the corresponding will be selected. |
| r | number | \-180.0000 to 180.0000 | The degree of map rotation. Only applies when arctic or antarctic projection is selected. |
| df | boolean | *true* or *false* | If true value is set, distraction free mode will be activated. Distraction free mode is disabled by default and can be toggled from the Information toolbar menu. |
| em | boolean | *true* or *false* | If true value is set, embed mode will be activated. Embed mode is disabled by default. |
| tr | string | *tour\_id* | The id of the tour story to load. Stories will load from step 1\. |
| abt | string | *on* | Indicates whether the about modal is open or not. Allows for permalinks that have the about page open |

## **2.3 CMR (Common Metadata Repository)**

### **Role**

Authoritative metadata source using UMM model.  
CMR MCP Available on: "[https://w4hu71445m.execute-api.us-east-1.amazonaws.com/mcp/cmr/mcp](https://w4hu71445m.execute-api.us-east-1.amazonaws.com/mcp/cmr/mcp)",  
Allowed\_tools: "search\_collections", "get\_collection\_metadata"

## **2.4 Earthdata Landing Pages Links**

### **Role**

Dataset and granule discovery handoff and Landing Page link if users ask for it. 

### **Agent Behavior**

* Generate smart links  
* Landing page links  
* Pass:  
  * Dataset ID  
  * Spatial filters  
  * Temporal filters

### **Explicitly Out-of-Scope**

* Automated download  
* Subsetting execution  
* Harmony workflows  
* OPeNDAP calls

## **2.5 EONET (Event Context)**

### **Provides**

* Event title  
* Geometry  
* Time window  
* Category  
* External source links

Public-only.

## **2.6 Science Discovery Engine (SDE)**

SDE may serve as:

* Last fallback for Dataset expansion beyond Worldview-indexed content and CMR  
* Cross-catalog semantic discovery

## **2.7 Worldview Layer Vector DB**

### **Purpose**

Internal semantic index for:

* Layer descriptions  
* Intent-to-layer mapping  
* Proxy detection  
* Fill in missing information from NASA GIBS API.

### **Not Authoritative**

Scientific authority remains CMR.

## **2.8 Tool for document Fetching and Document**

Purpose: Once the dataset is identified to be relevant or is a candidate to be used, this tool will be used to fetch the ATBD User guide if it exists.   
Input will be the concept ID which will be needed for this tool. 

# **4\. Comparison Mode Support**

Supported Modes:

| Mode | Same Layer Diff Date | Different Layers Same Date |
| ----- | ----- | ----- |
| Swipe | Yes | Yes |
| Spy | Yes | Yes |
| Opacity | Yes | Yes |

# **5\. Operational Constraints**

* Rate limits exist one query per second)  
* Avoid bulk tile iteration  
* Monitor 429/503 responses  
* Conservative throttling  
* Max time series length- decision based on per dataset

# **6\. Known System Constraints**

### Visualization and Statistics: All the visualization and statistics is constrained by query parameter acceptable values in Worldview URL.

# **7\. Explicitly Out-of-Scope**

* Raw granule retrieval  
* Server-side modeling  
* Prediction  
* Persistent user profiling  
* OPeNDAP workflows  
* Authenticated workflows