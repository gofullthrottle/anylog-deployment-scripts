#-------------------------------------------------------------------------------------------------
# Associate between a user and a set of permissions. This step needs to be done with root credentials
#-------------------------------------------------------------------------------------------------
# process !local_scripts/deployment_scripts/authentication/assignment_user.al

:set-params:
on error ignore
root_password = passwd
if $ROOT_PASSWORD  then set root_password = $ROOT_PASSWORD
policy_name = !company_name + " root policy"

# these values need to change when adding a user that's not in root
policy_user_type = !user_type
policy_user_name = !user_name

is_policy = blockchain get assignment where type=!policy_user_type and name=!policy_user_name and company=!company_name
if !is_policy goto end-script

:get-keys:
root_private_key = get private key where keys_file = root_keys
if not !root_private_key then goto private-key-error


:get-ids:
<member_certificate = blockchain get member where
    type = !policy_user_type and
    name = !policy_user_name and
    company = !company_name
bring [member][public_key]>

if not !member_certificate then goto certificate-error

<permission_id = blockchain get permissions where
    name = "limited restrictions" and
    company = !company_name
bring [permissions][id]>

if not !permission-id then goto permission-id-error

:declare-policy:
<new_policy = {"assignment" : {
    "name" : !policy_user_name,
    "permissions"  : !permission_id,
    "members"  : [!member_certificate]
}}>

:prepare-policy:
on error goto prepare-policy-error
new_policy = id sign !new_policy where key = !root_private_key and password = !root_password
validate_policy = json !new_policy
if not !validate_policy then goto prepare-policy-error

:declare-policy:
on error call declare-policy-error
blockchain prepare policy !new_policy
blockchain insert where policy=!new_policy and local=true and master=!ledger_conn

:end-script:
end script

:private-key-error:
echo "Failed to get private key rom generated root key"
goto end-script


:certificate-error:
echo "Failed to get public key for node policy"
goto end-script

:permission-id-error:
echo "Failed locate permission ID to associate the node against"
goto end-script

:public-key-error:
echo "Missing public key, cannot create valid member policy"
goto end-script

:prepare-policy-error:
echo "Failed to prepare member root policy for publishing on blockchain"
goto end-script

:declare-policy-error:
echo "Error: Failed to declare policy for root member"
returns
