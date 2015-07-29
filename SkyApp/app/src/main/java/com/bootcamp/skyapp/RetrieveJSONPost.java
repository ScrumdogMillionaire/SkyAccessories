package com.bootcamp.skyapp;

import android.content.Context;
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
        httppost.setHeader("Content-type", "application/x-www-form-urlencoded");

        InputStream inputStream = null;
        String result = null;
        try {
            List<NameValuePair> nameValuePairs = new ArrayList<NameValuePair>(2);
            nameValuePairs.add(new BasicNameValuePair(url[1], url[2]));
            nameValuePairs.add(new BasicNameValuePair(url[3], url[4]));
            httppost.setEntity(new UrlEncodedFormEntity(nameValuePairs));

            if (url[5] != null) {
                httppost.setHeader("Authorization", "Token " + url[5]);
            }

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

            Log.d("Raw output is: ", result);

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

    public static void tryLogin(String user, String password, Context ctx) throws Exception {
        JSONArray jarry = new JSONArray();

        AsyncTask task = new RetrieveJSONPost().execute(ctx.getString(R.string.ip) + "api-auth/", "email_or_username", user, "password", password, null);

        jarry = (JSONArray) task.get();

        Log.d("LOgin json", jarry.getJSONObject(0).toString());

        String token = jarry.getJSONObject(0).get("token").toString();
        String id = jarry.getJSONObject(0).get("user_id").toString();
        int points = jarry.getJSONObject(0).getInt("reward_points");
        String email = jarry.getJSONObject(0).get("email").toString();
        String username = jarry.getJSONObject(0).get("username").toString();
        String firstName = jarry.getJSONObject(0).get("first_name").toString();
        String lastName = jarry.getJSONObject(0).get("last_name").toString();

        User.makeUser(token, id, points, email, username, firstName, lastName);
        //User.makeUser(token, id, 2001, "tim@tim.tim", "timmy", "Timothy", "Timpson");

    }

    public static void placeOrder(String token, String userID, String productID, Context ctx) {
        //AsyncTask task = new RetrieveJSONPost().execute(ctx.getString(R.string.ip) + "api/place-order/", "user_id", userID, "prod_id", productID, token);
    }
}
