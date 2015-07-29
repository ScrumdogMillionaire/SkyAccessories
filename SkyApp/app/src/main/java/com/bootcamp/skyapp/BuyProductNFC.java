package com.bootcamp.skyapp;

import android.app.Activity;
import android.content.Intent;
import android.nfc.NdefMessage;
import android.nfc.NdefRecord;
import android.nfc.NfcAdapter;
import android.os.Parcelable;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.ObjectInputStream;
import java.io.UnsupportedEncodingException;


public class BuyProductNFC extends Activity {

    NdefMessage[] msgs;
    NdefRecord[] records;
    Product watch;
    String watchId;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_buy_product_nfc);
    }

    public void onResume() {
        super.onResume();

        Intent NFC = getIntent();

        if (NfcAdapter.ACTION_NDEF_DISCOVERED.equals(NFC.getAction())) {
            Parcelable[] rawMsgs = NFC.getParcelableArrayExtra(NfcAdapter.EXTRA_NDEF_MESSAGES);
            if (rawMsgs != null) {
                msgs = new NdefMessage[rawMsgs.length];
                for (int i = 0; i < rawMsgs.length; i++) {
                    msgs[i] = (NdefMessage) rawMsgs[i];
                    records = msgs[i].getRecords();
                    try { //TODO Improve to allow loop through records
                        watchId = new String(records[0].getPayload(), "US-ASCII");
                        if(watchId.length() > 0){
                            loadProduct(watchId);
                        }
                    } catch (UnsupportedEncodingException e) {
                        e.printStackTrace();
                    }
                }

                ImageView productPicture = (ImageView) findViewById(R.id.productPicture);
                new ImageDownloader(productPicture).execute(getString(R.string.ip) + watch.getPictureURL());

                try {
                    FileInputStream fis = openFileInput("userstate");
                    ObjectInputStream is = new ObjectInputStream(fis);
                    User restoredUser = (User) is.readObject();
                    is.close();
                    fis.close();

                    User.makeUser(restoredUser.getToken(), restoredUser.getId(), restoredUser.getPoints(), restoredUser.getEmail(), restoredUser.getUsername(), restoredUser.getFirstName(), restoredUser.getLastName());
                    Log.d("User loaded success:", User.getInstance().getPoints() + "");

                    TextView text = (TextView) findViewById(R.id.text);
                    text.setText("Do you wish to buy this product?");

                    Button order = (Button) findViewById(R.id.orderButton);
                    order.setVisibility(View.VISIBLE);

                    Button cancel = (Button) findViewById(R.id.noOrder);
                    cancel.setVisibility(View.VISIBLE);

                    Button login = (Button) findViewById(R.id.loginButton);
                    login.setVisibility(View.INVISIBLE);
                } catch (Exception e){
                    e.printStackTrace();
                }
            }
        }
        //process the msgs array
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_buy_product_nfc, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    private void loadProduct(String payloadString){
        watch = RetrieveJSON.getProduct(Integer.parseInt(payloadString), this);
    }



    public void orderProduct(View v){
        try {
            RetrieveJSONPost.placeOrder(User.getInstance().getToken(), User.getInstance().getId(), watchId, this);

            Toast.makeText(
                    this,
                    "Product ordered",
                    Toast.LENGTH_SHORT
            ).show();

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public void loadMenu(View v){
        Intent resultIntent = new Intent(this, MainMenu.class);
        startActivity(resultIntent);
    }

    public void loadLogin(View v){
        Intent resultIntent = new Intent(this, LandingActivity.class);
        startActivity(resultIntent);
    }
}
