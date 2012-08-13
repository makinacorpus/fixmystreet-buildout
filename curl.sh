#!/usr/bin/env bash
url="${FMS_URL:-"https://ville.terralego.com/open311/v2"}"
latlong="${LATLNG:-"lat=36.81873999&lon=10.16598"}"
curl() {
    local method=$1
    shift
    cmd="$(which curl)\
        --user "$FMS_USER:$FMS_PASSWORD"\
        -v --insecure \
        -X $method $@"
    echo "Running :"
    echo "  $cmd"
    $cmd
}
case $1 in
    jur)
        curl GET "$url/jurisdictions.json?api_key=$API_KEY&api_pass=$API_PASS"
        ;;
    cat)
        curl GET "$url/services.json?api_key=$API_KEY&api_pass=$API_PASS&$latlong"
        ;;
    reports)
        curl GET "$url/requests.json?api_key=$API_KEY&api_pass=$API_PASS&service_code=20&email=tazzzz333%40sfgov.edu&device_id=iphone2111&first_name=taz&last_name=taz&phone=5555555&description=Aaaaaaaa&$latlong"
        ;;
    newreport)
        curl POST "$url/requests.json" \
            -d"title=taazzz&api_key=$API_KEY&api_pass=$API_PASS&service_code=20&email=tazzzz333%40sfgov.edu&device_id=iphone2111&first_name=taz&last_name=taz&phone=5555555&description=Aaaaaaaa&$latlong"
        ;;
    *)
        echo "Prior to use do :"
        echo "    export FMS_PASSWORD="x" FMS_USER="x" API_KEY="x" API_PASS="x" [FMS_URL="$url"]"
        echo "$0 jur|newreport|cat"
        ;;
esac
