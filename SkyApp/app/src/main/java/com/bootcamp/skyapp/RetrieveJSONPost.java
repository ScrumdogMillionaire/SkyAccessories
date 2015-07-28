package com.bootcamp.skyapp;

import android.os.AsyncTask;
import android.util.Log;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.params.BasicHttpParams;
import org.apache.http.params.HttpConnectionParams;
import org.apache.http.params.HttpParams;
import org.json.JSONArray;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by tll01 on 28/07/2015.
 */
public class RetrieveJSONPost extends AsyncTask<String, Integer, JSONArray> {

    protected JSONArray doInBackground(String... url) {
        HttpParams httpParameters = new BasicHttpParams();
        int timeoutConnection = 3000;
        HttpConnectionParams.setConnectionTimeout(httpParameters, timeoutConnection);
        int timeoutSocket = 5000;
        HttpConnectionParams.setSoTimeout(httpParameters, timeoutSocket);
        DefaultHttpClient httpclient = new DefaultHttpClient(httpParameters);
        HttpPost httppost = new HttpPost(url[0]);
        // Depends on your web service
        httppost.setHeader("Content-type", "application/json");

        InputStream inputStream = null;
        String result = null;
        try {
            List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>(2);
            nameValuePairs.add(new BasicNameValuePair("email_or_username", "tim"));
            nameValuePairs.add(new BasicNameValuePair("password", "password"));
            httppost.setEntity(new UrlEncodedFormEntity(nameValuePairs));
            System.out.println(httppost.getParams());

            HttpResponse response = httpclient.execute(httppost);

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

    public static void tryLogin(){
        JSONArray jarry = new JSONArray();

        AsyncTask task = new RetrieveJSONPost().execute("http://192.168.1.14:3001/api-auth/");
        try {
            jarry = (JSONArray) task.get();
            System.out.print(jarry);

            //String name = jarry.getJSONObject(0).get("name").toString();
            //String url = jarry.getJSONObject(0).get("url").toString();


        } catch (Exception e) {
            e.printStackTrace();
        }


    }
}
