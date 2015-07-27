package com.bootcamp.skyapp;

import android.os.AsyncTask;
import android.util.Log;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.params.BasicHttpParams;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.net.URL;
import java.util.ArrayList;
import java.util.concurrent.ExecutionException;

/**
 * Created by tll01 on 27/07/2015.
 */

public class RetrieveJSON extends AsyncTask<String, Integer, JSONArray> {

    protected JSONArray doInBackground(String... url) {

        DefaultHttpClient   httpclient = new DefaultHttpClient(new BasicHttpParams());
        HttpGet httpget = new HttpGet(url[0]);
        // Depends on your web service
        httpget.setHeader("Content-type", "application/json");

        InputStream inputStream = null;
        String result = null;
        try {
            HttpResponse response = httpclient.execute(httpget);
            HttpEntity entity = response.getEntity();

            inputStream = entity.getContent();
            // json is UTF-8 by default
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream, "UTF-8"), 8);
            StringBuilder sb = new StringBuilder();

            String line = null;
            while ((line = reader.readLine()) != null)
            {
                sb.append(line + "\n");
            }
            result = sb.toString();
            JSONArray jArray = new JSONArray(result);

            return jArray;

        } catch (Exception e) {
            Log.d("Something", "SOmething ELSE", e);
        } finally {
            try{if(inputStream != null)inputStream.close();}catch(Exception squish){}
        }

        return new JSONArray();
    }

    protected void onProgressUpdate(Integer... progress) {

    }

    protected void onPostExecute(JSONArray result) {

    }

    public static ArrayList<Marker> getMarkers() {
        JSONArray jarry = new JSONArray();
        ArrayList<Marker> markers = new ArrayList<Marker>();

        AsyncTask task = new RetrieveJSON().execute("http://demo1828387.mockable.io/markers");
        try {
            jarry = (JSONArray) task.get();

            for (int i = 0; i < jarry.length(); i++) {

                Double latitude = jarry.getJSONObject(i).getDouble("lat");
                Double longitude = jarry.getJSONObject(i).getDouble("long");
                String description = jarry.getJSONObject(i).get("description").toString();

                Marker store = new Marker(latitude, longitude, description);

                markers.add(store);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        return markers;
    }

    public static Product getProduct(int productID){
        JSONArray jarry = new JSONArray();
        Product watch = new Product("", "");

        AsyncTask task = new RetrieveJSON().execute("http://demo1828387.mockable.io/product/"+productID);
        try {
            jarry = (JSONArray) task.get();

            String name = jarry.getJSONObject(0).get("name").toString();
            String url = jarry.getJSONObject(0).get("url").toString();

           watch = new Product(name, url);
        } catch (Exception e) {
            e.printStackTrace();
        }

        return watch;
    }

}
