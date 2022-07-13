from multiprocessing import context
from django.shortcuts import render
from brain import niftyprice,HDFCBANK,RELIANCE,INFY,HDFC,ICICIBANK,TCS,KOTAKBANK,ITC,stock_details,HUL,MM

# Create your views here.

def index(request):
    context = {
        'price':niftyprice.Nifty,
        'nifty_chg':niftyprice.nifty_ch,
        #HDFCBANK
        'HDFCBANK_points':stock_details.stock_pt[0],
        'HDFCBANK_LTP':stock_details.stock_val[0],
        'HDFCBANK_CHG':stock_details.stock_chg[0],
        #RELIANCE
        'RELIANCE_points':stock_details.stock_pt[1],
        'RELIANCE_LTP':stock_details.stock_val[1],
        'RELIANCE_CHG':stock_details.stock_chg[1],
        #INFY
        'INFY_points':stock_details.stock_pt[2],
        'INFY_LTP':stock_details.stock_val[2],
        'INFY_CHG':stock_details.stock_chg[2],
        #HDFC
        'HDFC_points':stock_details.stock_pt[3],
        'HDFC_LTP':stock_details.stock_val[3],
        'HDFC_CHG':stock_details.stock_chg[3],
        #ICICIBANK
        'ICICIBANK_points':stock_details.stock_pt[4],
        'ICICIBANK_LTP':stock_details.stock_val[4],
        'ICICIBANK_CHG':stock_details.stock_chg[4],
        #TCS
        'TCS_points':stock_details.stock_pt[5],
        'TCS_LTP':stock_details.stock_val[5],
        'TCS_CHG':stock_details.stock_chg[5],
        #KOTAKBANK
        'KOTAKBANK_points':stock_details.stock_pt[6],
        'KOTAKBANK_LTP':stock_details.stock_val[6],
        'KOTAKBANK_CHG':stock_details.stock_chg[6],
        #HUL
        #'HUL_points':HUL.HUL_points,
        #'HUL_LTP':HUL.HUL_val,
        #'HUL_CHG':HUL.HUL_change,
        #ITC
        'ITC_points':stock_details.stock_pt[7],
        'ITC_LTP':stock_details.stock_val[7],
        'ITC_CHG':stock_details.stock_chg[7],
        #AXISBANK
        'AXISBANK_points':stock_details.stock_pt[8],
        'AXISBANK_LTP':stock_details.stock_val[8],
        'AXISBANK_CHG':stock_details.stock_chg[8],
        #LT
        'LT_points':stock_details.stock_pt[9],
        'LT_LTP':stock_details.stock_val[9],
        'LT_CHG':stock_details.stock_chg[9],
        #SBIN
        'SBIN_points':stock_details.stock_pt[10],
        'SBIN_LTP':stock_details.stock_val[10],
        'SBIN_CHG':stock_details.stock_chg[10],
        #BAJFINANCE
        'BAJFINANCE_points':stock_details.stock_pt[11],
        'BAJFINANCE_LTP':stock_details.stock_val[11],
        'BAJFINANCE_CHG':stock_details.stock_chg[11],
        #BHARTIARTL
        'BHARTIARTL_points':stock_details.stock_pt[12],
        'BHARTIARTL_LTP':stock_details.stock_val[12],
        'BHARTIARTL_CHG':stock_details.stock_chg[12],
        #ASIANPAINT
        'ASIANPAINT_points':stock_details.stock_pt[13],
        'ASIANPAINT_LTP':stock_details.stock_val[13],
        'ASIANPAINT_CHG':stock_details.stock_chg[13],
        #HCLTECH
        'HCLTECH_points':stock_details.stock_pt[14],
        'HCLTECH_LTP':stock_details.stock_val[14],
        'HCLTECH_CHG':stock_details.stock_chg[14],
        #MARUTI
        'MARUTI_points':stock_details.stock_pt[15],
        'MARUTI_LTP':stock_details.stock_val[15],
        'MARUTI_CHG':stock_details.stock_chg[15],
        #ULTRACEMCO
        'ULTRACEMCO_points':stock_details.stock_pt[16],
        'ULTRACEMCO_LTP':stock_details.stock_val[16],
        'ULTRACEMCO_CHG':stock_details.stock_chg[16],
        #SUNPHARMA
        'SUNPHARMA_points':stock_details.stock_pt[17],
        'SUNPHARMA_LTP':stock_details.stock_val[17],
        'SUNPHARMA_CHG':stock_details.stock_chg[17],
        #TITAN
        'TITAN_points':stock_details.stock_pt[18],
        'TITAN_LTP':stock_details.stock_val[18],
        'TITAN_CHG':stock_details.stock_chg[18],
        #TECHM
        'TECHM_points':stock_details.stock_pt[19],
        'TECHM_LTP':stock_details.stock_val[19],
        'TECHM_CHG':stock_details.stock_chg[19],
        #WIPRO
        'WIPRO_points':stock_details.stock_pt[20],
        'WIPRO_LTP':stock_details.stock_val[20],
        'WIPRO_CHG':stock_details.stock_chg[20],
        #NESTLEIND
        'NESTLEIND_points':stock_details.stock_pt[21],
        'NESTLEIND_LTP':stock_details.stock_val[21],
        'NESTLEIND_CHG':stock_details.stock_chg[21],
        #TATASTEEL
        'TATASTEEL_points':stock_details.stock_pt[22],
        'TATASTEEL_LTP':stock_details.stock_val[22],
        'TATASTEEL_CHG':stock_details.stock_chg[22],
        #BAJAJFINSV
        'BAJAJFINSV_points':stock_details.stock_pt[23],
        'BAJAJFINSV_LTP':stock_details.stock_val[23],
        'BAJAJFINSV_CHG':stock_details.stock_chg[23],
        #HDFCLIFE
        'HDFCLIFE_points':stock_details.stock_pt[24],
        'HDFCLIFE_LTP':stock_details.stock_val[24],
        'HDFCLIFE_CHG':stock_details.stock_chg[24],
        #POWERGRID
        'POWERGRID_points':stock_details.stock_pt[25],
        'POWERGRID_LTP':stock_details.stock_val[25],
        'POWERGRID_CHG':stock_details.stock_chg[25],
        #GRASIM
        'GRASIM_points':stock_details.stock_pt[26],
        'GRASIM_LTP':stock_details.stock_val[26],
        'GRASIM_CHG':stock_details.stock_chg[26],
        #DRREDDY
        'DRREDDY_points':stock_details.stock_pt[27],
        'DRREDDY_LTP':stock_details.stock_val[27],
        'DRREDDY_CHG':stock_details.stock_chg[27],
        #INDUSINDBK
        'INDUSINDBK_points':stock_details.stock_pt[28],
        'INDUSINDBK_LTP':stock_details.stock_val[28],
        'INDUSINDBK_CHG':stock_details.stock_chg[28],
        #TATAMOTORS
        'TATAMOTORS_points':stock_details.stock_pt[29],
        'TATAMOTORS_LTP':stock_details.stock_val[29],
        'TATAMOTORS_CHG':stock_details.stock_chg[29],
        #ADANIPORTS
        'ADANIPORTS_points':stock_details.stock_pt[30],
        'ADANIPORTS_LTP':stock_details.stock_val[30],
        'ADANIPORTS_CHG':stock_details.stock_chg[30],
        #NTPC
        'NTPC_points':stock_details.stock_pt[31],
        'NTPC_LTP':stock_details.stock_val[31],
        'NTPC_CHG':stock_details.stock_chg[31],
        #BAJAJ-AUTO
        'BAJAJAUTO_points':stock_details.stock_pt[32],
        'BAJAJAUTO_LTP':stock_details.stock_val[32],
        'BAJAJAUTO_CHG':stock_details.stock_chg[32],
        #HINDALCO
        'HINDALCO_points':stock_details.stock_pt[33],
        'HINDALCO_LTP':stock_details.stock_val[33],
        'HINDALCO_CHG':stock_details.stock_chg[33],
        #DIVISLAB
        'DIVISLAB_points':stock_details.stock_pt[34],
        'DIVISLAB_LTP':stock_details.stock_val[34],
        'DIVISLAB_CHG':stock_details.stock_chg[34],
        #JSWSTEEL
        'JSWSTEEL_points':stock_details.stock_pt[35],
        'JSWSTEEL_LTP':stock_details.stock_val[35],
        'JSWSTEEL_CHG':stock_details.stock_chg[35],
        #BRITANNIA
        'BRITANNIA_points':stock_details.stock_pt[36],
        'BRITANNIA_LTP':stock_details.stock_val[36],
        'BRITANNIA_CHG':stock_details.stock_chg[36],
        #CIPLA
        'CIPLA_points':stock_details.stock_pt[37],
        'CIPLA_LTP':stock_details.stock_val[37],
        'CIPLA_CHG':stock_details.stock_chg[37],
        #BPCL
        'BPCL_points':stock_details.stock_pt[38],
        'BPCL_LTP':stock_details.stock_val[38],
        'BPCL_CHG':stock_details.stock_chg[38],
        #SHREECEM
        'SHREECEM_points':stock_details.stock_pt[39],
        'SHREECEM_LTP':stock_details.stock_val[39],
        'SHREECEM_CHG':stock_details.stock_chg[39],
        #HEROMOTOCO
        'HEROMOTOCO_points':stock_details.stock_pt[40],
        'HEROMOTOCO_LTP':stock_details.stock_val[40],
        'HEROMOTOCO_CHG':stock_details.stock_chg[40],
        #ONGC
        'ONGC_points':stock_details.stock_pt[41],
        'ONGC_LTP':stock_details.stock_val[41],
        'ONGC_CHG':stock_details.stock_chg[41],
        #EICHERMOT
        'EICHERMOT_points':stock_details.stock_pt[42],
        'EICHERMOT_LTP':stock_details.stock_val[42],
        'EICHERMOT_CHG':stock_details.stock_chg[42],
        #UPL
        'UPL_points':stock_details.stock_pt[43],
        'UPL_LTP':stock_details.stock_val[43],
        'UPL_CHG':stock_details.stock_chg[43],
        #SBILIFE
        'SBILIFE_points':stock_details.stock_pt[44],
        'SBILIFE_LTP':stock_details.stock_val[44],
        'SBILIFE_CHG':stock_details.stock_chg[44],
        #COALINDIA
        'COALINDIA_points':stock_details.stock_pt[45],
        'COALINDIA_LTP':stock_details.stock_val[45],
        'COALINDIA_CHG':stock_details.stock_chg[45],
        #TATACONSUM
        'TATACONSUM_points':stock_details.stock_pt[46],
        'TATACONSUM_LTP':stock_details.stock_val[46],
        'TATACONSUM_CHG':stock_details.stock_chg[46],
        #APOLLOHOSP
        'APOLLOHOSP_points':stock_details.stock_pt[47],
        'APOLLOHOSP_LTP':stock_details.stock_val[47],
        'APOLLOHOSP_CHG':stock_details.stock_chg[47],
        #HUL
        'HUL_points':HUL.stock_points,
        'HUL_LTP':HUL.HUL_price,
        'HUL_CHG':HUL.HUL_change,
        #M&M
        'MM_points':MM.stock_points,
        'MM_LTP':MM.MM_price,
        'MM_CHG':MM.MM_change,


    }
    return render(request, 'index.html',context)