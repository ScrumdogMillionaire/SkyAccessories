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
import android.widget.Toast;

import java.io.UnsupportedEncodingException;


public class BuyProductNFC extends Activity {

    NdefMessage[] msgs;
    NdefRecord[] records;
    String productID;

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
                    try {
                        for (int j = 0; j < records.length; j++) {
                            String payloadString = new String(records[j].getPayload(), "US-ASCII");
                            if(payloadString.length() > 0){
                                loadProduct(payloadString);
                            }
                        }
                    } catch (UnsupportedEncodingException e) {
                        e.printStackTrace();
                    }
                }

                Toast.makeText(
                        this,
                        "Product ID: " + productID,
                        Toast.LENGTH_SHORT
                ).show();
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
        productID = payloadString;

        //TODO change gui
    }
}
