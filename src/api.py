# -*- coding: utf-8 -*-
import requests

BASE_URL = 'http://192.168.102.180:8075/api'


def get_service_list() -> list:
    """Load a list of existing Kubernetes services

    Returns:
        list: List of currently running services.
    """

    url = f'{BASE_URL}/service'
    return requests.get(url).json()


def get_service_info(ID: str) -> dict:
    """Load information from a specific Kubernetes service using a unique ID value

    Args:
        ID (str): Kubernetes Service ID

    Returns:
        dict: Service information in JSON format
    """

    url = BASE_URL + f'/service' + '/' + ID
    return requests.get(url).json()


def get_service_ID(NameSpace: str) -> str:
    """Find the unique ID value using the service's NameSpace.\n
    (Note: Duplicate NameSpaces may not produce the desired results.)

    Args:
        NameSpace (str): Kubernetes Service Namespace

    Returns:
        str: Service ID found from Namespace
    """

    ID = 'Not found'
    for service in get_service_list():
        if service['Name'] == NameSpace:
            ID = service['ID']
            break
    return ID


def get_service_url(NameSpace: str) -> list:
    """Load the URL of the service using the service's NameSpace

    Args:
        NameSpace (str): Kubernetes Service Namespace

    Returns:
        list: Service URLs found from Namespace
    """

    ID = get_service_ID(NameSpace=NameSpace)
    data = get_service_info(ID=ID)
    return data['URL']
