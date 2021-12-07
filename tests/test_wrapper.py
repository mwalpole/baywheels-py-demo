import baywheels.data.s3.wrapper as wrapper


class TestTripData:
    def test_get_tripdata_filenames(self):
        res = wrapper.get_tripdata_filenames()
        assert len(res) > 1

    def test_get_latest_tripdata_filename(self):
        res = wrapper.get_latest_tripdata_filename()
        assert res.endswith('.zip')

    def test_save_url_to_local_produces_one_zip_file(self):
        res = wrapper.save_url_to_local()
        assert res[0].endswith('.zip')

    def test_save_url_to_local_with_uncompressed_writes_a_csv_file(self):
        res = wrapper.save_url_to_local(uncompress=True)
        assert res[0].endswith('.csv')