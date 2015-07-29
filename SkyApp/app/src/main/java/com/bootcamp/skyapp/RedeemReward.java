package com.bootcamp.skyapp;

import android.app.Activity;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;


public class RedeemReward extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_redeem_reward);

        int points = User.getInstance().getPoints();

        if (points < 1000){
            Button reward1 = (Button) findViewById(R.id.button1);
            reward1.setClickable(false);
            reward1.setBackgroundResource(R.drawable.pause);// TODO: change pause drawable to grey image (square icons)
        }

        if (points < 2000){
            Button reward2 = (Button) findViewById(R.id.button2);
            reward2.setClickable(false);
            reward2.setBackgroundResource(R.drawable.pause);
        }

        if (points < 3000){
            Button reward3 = (Button) findViewById(R.id.button3);
            reward3.setClickable(false);
            reward3.setBackgroundResource(R.drawable.pause);
        }

        if (points < 4000){
            Button reward4 = (Button) findViewById(R.id.button4);
            reward4.setClickable(false);
            reward4.setBackgroundResource(R.drawable.pause);
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_redeem_reward, menu);
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
}
