#-----------------------------------------------------------------------------------------------------------------------
# {
#  "apiVersion": "v2",
#  "id": "707564c4-6818-4746-9c54-219a0fd110c6",
#  "deviceName": "ba-virtual",
#  "profileName": "BuildingAutomationVirtualDevice",
#  "sourceName": "AvgTemp",
#  "origin": 1686087247849269800,
#  "readings": [
#    {
#      "id": "42700bdd-4525-443f-88dd-22c488011b65",
#      "origin": 1686087247849269800,
#      "deviceName": "ba-virtual",
#      "resourceName": "AvgTemp",
#      "profileName": "BuildingAutomationVirtualDevice",
#      "valueType": "Float32",
#      "units": "°F",
#      "value": "7.934139e+01"
#    }
#  ]
#-----------------------------------------------------------------------------------------------------------------------
# process !local_scripts/sample_code/edgex_demo.al

if not !mqtt_topic_dbms and not !default_dbms then set mqtt_topic_dbms = test
else if not !mqtt_topic_dbms and !default_dbms then mqtt_topic_dbms =  !default_dbms

topic_name = LATERAL
is_policy = blockchain get mapping where id = !topic_name
if not !is_policy then
<do mapping_policy = {
    "mapping": {
        "id": !topic_name,
        "dbms": !mqtt_topic_dbms,
        "table": "bring [sourceName]",
        "readings": "readings",
        "schema": {
            "timestamp" : {
                "bring": "[origin]",
                "default" : "now()",
                "type" : "timestamp",
                "apply" :  "epoch_to_datetime"
            },
            "reading_id": {
                "type": "string",
                "value": "bring [id]"
            },
            "units": {
                "type": "string",
                "value": "bring [units]",
                "default": ""
            },
            "value": [
                {
                    "condition": "if [sourceName] == Bool",
                    "type": "bool",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == FanStatus",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == Int8",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == Int16",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == Int32",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == Int64",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == LightOut1",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == LightOut2",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == LightOut3",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == LightOut4",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == Unit8",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == Unit16",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == Unit32",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "condition": "if [sourceName] == Unit64",
                    "type": "int",
                    "value": "bring [value]"
                },
                {
                    "type": "float",
                    "value": "bring [value]"
                }

            ]
        }
    }
}>
do test_policy = json !mapping_policy test
do if !test_policy == false then goto json-policy-error

on error call declare-policy-error
if !test_policy == true and not !is_policy
do blockchain prepare policy !mapping_policy
do blockchain insert where policy=!mapping_policy and local=true and master=!ledger_conn

<run mqtt client where broker=local and port=32150
    and log=false and topic=(name=!topic_name and policy=!topic_name)>

:end-script:
end script

:declare-params-error:
echo "Failed to declare one or more policies. Cannot continue..."
goto end-script

:connect-dbms-error:
echo "Failed to connect to MongoDB logical database " !mongo_db_name ". Cannot continue..."
goto end-script

:blobs-archiver-error:
echo "Failed to enable blobs archiver"
return

:json-policy-error:
echo "Invalid JSON format, cannot declare policy"
goto end-script

:declare-policy-error:
echo "Failed to declare policy on blockchain"
return


:mqtt-error:
echo "Failed to deploy MQTT process"
goto end-script
