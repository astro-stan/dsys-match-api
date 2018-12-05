#!/usr/bin/env python3

import urllib.parse as url
import requests
import json

class DsysMatch:
    def __init__(self, server_address: str, server_port: int = 80):
        """
        A simple wrapper over the dsys/match Web API.

        Parameters
        ----------
        server_address : str
            The server IP address, and scheme.
            Example: http://35.185.109.219
        server_port : int = 80
            The port on which dsys/match is listening.

        Returns
        -------
        None

        TODO
        ----
        - Add type & range guards


        """
        self.server_address = server_address.strip(
            '/') + ':' + str(server_port) + '/'

    def Add(self, image_path: str, file_path: str, metadata: str = None):
        """
        Adds an image signature to the database.

        Parameters
        ----------
        image_path : str
            The location, on disk for the image.
        filepath : str
            The path of the image signature in the database.
            If the path exists it will be overwritten with the
            new signature.
        metadata : str = None
            A JSON formatted str object featuring metadata to
            attach to the image.   

        Returns
        -------
        dict
        """
        image_binary = open(image_path, 'rb')
        payload = {
            'image': ('image', image_binary),
            'filepath': ('', file_path),
        }

        if (metadata != None):
            payload['metadata'] = ('', metadata)

        request_address = url.urljoin(self.server_address, '/add')
        return json.loads(requests.post(request_address, files=payload).text)

    def Delete(self, file_path: str):
        """
        Deletes an image signature from the database.

        Parameters
        ----------
        filepath : str
            The path of the image signature in the database.

        Returns
        -------
        dict
        """
        payload = {
            'filepath': file_path,
        }

        request_address = url.urljoin(self.server_address, '/delete')
        return json.loads(requests.delete(request_address, data=payload).text)

    def Search(self, image_path: str, all_orientations: bool = True):
        """
        Searches for a similar image in the database.
        Scores range from 0 to 100, with 100 being a perfect match.

        Parameters
        ----------
        image_path : str
            The location, on disk for the image.        
        all_orientations : bool = True
            Whether or not to search for similar 90 degree rotations of the image.           

        Returns
        -------
        dict
        """
        image_binary = open(image_path, 'rb')
        payload = {
            'image': ('image', image_binary),
            'all_orientations': ('', all_orientations),
        }

        request_address = url.urljoin(self.server_address, '/search')
        return json.loads(requests.post(request_address, files=payload).text)

    def Compare(self, image1_path: str, image2_path: str):
        """
        Compares two images, returning a score for their similarity.
        Scores range from 0 to 100, with 100 being a perfect match.

        Parameters
        ----------
        image1_path : str
            The location, on disk for image1.
        image2_path : str
            The location, on disk for image2.            

        Returns
        -------
        dict
        """
        image1_binary = open(image1_path, 'rb')
        image2_binary = open(image2_path, 'rb')

        payload = {
            'image1': ('image1', image1_binary),
            'image2': ('image2', image2_binary),
        }

        request_address = url.urljoin(self.server_address, '/compare')
        return json.loads(requests.post(request_address, files=payload).text)

    def Count(self):
        """
        Count the number of image signatures in the database.
        """
        request_address = url.urljoin(self.server_address, '/count')
        return json.loads(requests.get(request_address).text)

    def List(self, offset: int = 0, limit: int = 20):
        """
        Lists the file paths for the image signatures in the database.

        Parameters
        ----------
        offset : int = 0
            The location in the database to begin listing image paths.
        limit : int = 20
            The number of image paths to retrieve.

        Returns
        -------
        dict
        """
        params = {
            'offset': offset,
            'limit': limit
        }
        request_address = url.urljoin(self.server_address, '/list')
        return json.loads(requests.get(request_address, params=params).text)

    def Ping(self):
        """
        Check for the health of the server.
        """
        request_address = url.urljoin(self.server_address, '/ping')
        return json.loads(requests.get(request_address).text)


if __name__ == '__main__':
    raise SystemExit(
        "Please import this module into a python script and use it from there..."
    )
