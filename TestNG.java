package Case;

import java.util.Set;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.WebDriver;

import org.openqa.selenium.firefox.FirefoxDriver;

import org.testng.Assert;

import org.testng.annotations.BeforeMethod;

import org.testng.annotations.AfterMethod;

import org.testng.annotations.Test;

import Method.MethodLayer;

import Object.ObjectLayer;

 

public class TestCase {

         private static final String FreshText = null;

         private WebDriver driver;

         private String baseUrl;

         String username="SXB";

         String password="123456";

        

         @BeforeMethod

         public void setUp() throws Exception{

                   driver=new FirefoxDriver();

                   driver.manage().window().maximize();

                   baseUrl="https://192.168.5.161";

                   driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

                   driver.get(baseUrl);

                   MethodLayer.login(driver,username,password);

         }

        

         @Test(enabled=true)      //登陆正常

         public void Login() throws Exception{

                   Thread.sleep(5000);

                   String text=MethodLayer.login_info(driver);

                   Assert.assertEquals(text, "欢迎您！ "+username);

                   MethodLayer.logout(driver);

         }

        

         @Test(enabled=true)      //历史监控页面正常打开

         public void BusinessMonitorTest() throws Exception{

                   String home_handle=driver.getWindowHandle();

                   String text=MethodLayer.BusinessMonitorMethod(driver);

                   Set<String>handles=driver.getWindowHandles();

                   for (String handle : handles){

                            if (handle.equals(home_handle)==false){

                                     driver.switchTo().window(handle);

                                     text=driver.getTitle();

                                     Assert.assertEquals(text,"历史监控-科来业务性能管理系统");

                                     }       

                            }  

                   }

        

         @Test(enabled=true)      //业务集中监控页面正常打开

         public void BusinessFocusTest() throws Exception{

                   String text=MethodLayer.BusinessFocusMethod(driver);

                   String FreshText=ObjectLayer.AutoFreshButton(driver).getText();

                   Assert.assertEquals(FreshText,"ON");

                   ObjectLayer.AutoFreshButton(driver).click();

                   Assert.assertEquals(text, "业务集中监控-科来业务性能管理系统");

         }

        

         @AfterMethod

         public void tearDown() throws Exception{

                   System.out.println("Browser Will Closed In 5 Seconds");

                   Thread.sleep(5000);

                   driver.quit();

         }

 

}