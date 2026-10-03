import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "server")))

from app import app
from fastapi.testclient import TestClient

class TestCommunityHealthAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_health(self):
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["location"], "Semera, Afar, Ethiopia")

    def test_sync_records(self):
        data = [
            {"patient_name": "Amina Mohammed", "woreda": "Dubti", "muac_cm": 12.1}
        ]
        resp = self.client.post("/sync", json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["received_count"], 1)

if __name__ == "__main__":
    unittest.main()
