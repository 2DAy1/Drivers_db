class TestViews:

    def test_report(self, client):
        url = "/api/v1/report/"

        # test json format
        response_json = client.get(url, query_string={'format': "json"})
        assert response_json.status_code == 200
        assert response_json.headers['Content-Type'] == "application/json"

        # test xml format
        response_xml = client.get(url, query_string={'format': "xml"})
        assert response_xml.status_code == 200
        assert response_xml.headers['Content-Type'] == "application/xml"

        # test order
        response_desc = client.get(url, query_string={'order': "desc"})
        response_ask = client.get(url, query_string={'order': "ask"})
        assert response_ask.status_code == 200
        assert response_desc.status_code == 200
        assert response_ask.json == response_desc.json[::-1]


        # r_format = ["json", "xml", ""]
        # r_order = ["desc", "ask", ""]
        # data = []
        # for i in r_format:
        #     for j in r_order:
        #         data.append({"format": i, "order": j})
        #
        # for i in data:
        #     response = client.get(url, params=i)
        #     assert response.status_code == 200