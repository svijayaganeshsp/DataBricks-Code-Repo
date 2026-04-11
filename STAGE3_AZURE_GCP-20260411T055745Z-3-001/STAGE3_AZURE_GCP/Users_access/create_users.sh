
#chmod 777 create_users.sh

#./create_users.sh inceptezdatascience2gmail.onmicrosoft.com 'Inceptez@123' wd36_de_group1


#!/bin/bash

DOMAIN="$1"
DEFAULT_PASSWORD="$2"
GROUP_NAME="$3"
CSV_FILE="users.csv"

if [ -z "$DOMAIN" ] || [ -z "$DEFAULT_PASSWORD" ] || [ -z "$GROUP_NAME" ]; then
    echo "Usage: ./create_users.sh <domain_suffix> <default_password> <group_name>"
    echo "Example: ./create_users.sh inceptezdatascience2gmail.onmicrosoft.com 'Inceptez@123' 'wd36_de_group1'"
    exit 1
fi

if [ ! -f "$CSV_FILE" ]; then
    echo "CSV file users.csv not found"
    exit 1
fi

GROUP_ID=$(az ad group show --group "$GROUP_NAME" --query id -o tsv 2>/dev/null)

if [ -z "$GROUP_ID" ]; then
    echo "Group does not exist. Creating group: $GROUP_NAME"

    GROUP_MAIL_NICKNAME=$(echo "$GROUP_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')

    GROUP_ID=$(az ad group create \
        --display-name "$GROUP_NAME" \
        --mail-nickname "$GROUP_MAIL_NICKNAME" \
        --query id \
        -o tsv)

    echo "Group created with ID: $GROUP_ID"
else
    echo "Using existing group: $GROUP_NAME"
fi

tail -n +2 "$CSV_FILE" | while IFS=',' read -r USERID DISPLAYNAME
do
    USERID=$(echo "$USERID" | xargs | tr '[:upper:]' '[:lower:]')
    DISPLAYNAME=$(echo "$DISPLAYNAME" | xargs)

    if [ -z "$USERID" ] || [ -z "$DISPLAYNAME" ]; then
        continue
    fi

    USER_PRINCIPAL_NAME="${USERID}@${DOMAIN}"

    echo "Creating user: $DISPLAYNAME ($USER_PRINCIPAL_NAME)"

    USER_OBJECT_ID=$(az ad user create \
        --display-name "$DISPLAYNAME" \
        --user-principal-name "$USER_PRINCIPAL_NAME" \
        --password "$DEFAULT_PASSWORD" \
        --force-change-password-next-sign-in true \
        --mail-nickname "$USERID" \
        --query id \
        -o tsv 2>/dev/null)

    if [ -z "$USER_OBJECT_ID" ]; then
        echo "Failed to create user: $USER_PRINCIPAL_NAME"
        echo "----------------------------------------"
        continue
    fi

    echo "Adding user to group: $GROUP_NAME"

    az ad group member add \
        --group "$GROUP_ID" \
        --member-id "$USER_OBJECT_ID" 2>/dev/null

    echo "----------------------------------------"
done